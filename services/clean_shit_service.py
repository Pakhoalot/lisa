#!/usr/bin/env python

#-*- coding:utf-8 -*-

''
import logging
import threading
from threading import Thread
import RPi.GPIO as GPIO
import time

import config
from sensors.distance_detector import DistanceDetector
from sensors.motor_hand_made import Motor
from sensors.switch import Switch
from services.service import Service

__author__ = 'PakhoLeung'

class CleanShitService(Service,Thread):
    __TAIL = 370
    __HEAD = 0
    __POSITION = None
    motor = None
    distanceDetector = None
    switch = None
    flag = 0 #当一时，电机不能动
    def __init__(self) -> None:
        super().__init__()
        self.motor = Motor(config.CSS_MOTOR_PWM_CHANNEL,
                           config.CSS_MOTOR_DIR_CHANNEL,
                           config.CSS_MOTOR_ENABLED_CHANNEL,
                           config.CSS_MOTOR_FREQUENT)
        self.distanceDetector = DistanceDetector(config.CSS_DD_TRIGER,
                                                 config.CSS_DD_ECHO)
        self.switch = Switch(config.CSS_SWITCH_CHANNEL)
        #设置版位置为零
        self.__POSITION = 0




    def run(self):

        #开启距离实时监测
        t1 = threading.Thread(target=self.detect,args=())
        t1.start()

        self.moveToHead()
        while self.__POSITION < self.__TAIL:
            if self.flag == 0:
                self.motor.setDirection(self.motor.LEFT)
                self.motor.forward()
                self.__POSITION = self.__POSITION+1
            elif self.flag == 1:
                logging.info("Cleaner is blocked. Reset and preapre to Restart")
                self.moveToHead()
                #当前方没物体时，重启机器
                while self.flag == 0:
                    pass
                logging.info("Clear. Begin to start")

        logging.info("Clean up.")
        time.sleep(3)
        self.moveToHead()


    def moveToHead(self):
        if self.__POSITION != self.__HEAD:
            self.motor.setDirection(self.motor.RIGHT)
            while self.__POSITION != 0:
                self.motor.forward()
    def moveToTail(self):
        if self.__POSITION != self.__TAIL:
            self.motor.setDirection(self.motor.LEFT)
            while self.__POSITION != 0:
                self.motor.forward()
    def startService(self):
        self.start()

    def detect(self):
        dis = 1000
        while True:
            time.sleep(0.5)
            dis = self.distanceDetector.getDistance()
            if dis < 30:
                self.flag = 1
                # if self.motor.getStatus() == self.motor.RUNNING:
                #     self.motor.pause()
            else :
                self.flag = 0

