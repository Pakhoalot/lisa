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
from sensors.motor import Motor
from services.service import Service

__author__ = 'PakhoLeung'

class CleanShitService(Service,Thread):
    motor = None
    distanceDetector = None
    flag = 0 #当一时，电机不能动
    def __init__(self) -> None:
        super().__init__()
        self.motor = Motor(config.MOTOR_PWM_CHANNEL,
                           config.MOTOR_DIR_CHANNEL,
                           config.MOTOR_ENABLED_CHANNEL,
                           config.MOTOR_FREQUENT)
        self.distanceDetector = DistanceDetector(config.DD_TRIGER,
                                                 config.DD_ECHO)




    def run(self):

        #开启距离实时监测
        t1 = threading.Thread(target=self.detect,args=())
        t1.start()
        time_pool = 0
        real_delay = time.time()
        begin = time.time()
        while time_pool < 10:
            if self.flag == 0:
                self.motor.start()
                time.sleep(0.01)
                time_pool = time_pool + (time.time()-begin)
                begin = time.time()
            elif self.flag == 1:
                self.motor.stop()
                time.sleep(0.01)
                begin = time.time()

        self.motor.stop()
        logging.info("clean ends. spend "+ str(time_pool)+ "s")
        logging.info("real delay"+str(time.time()-real_delay))


        time.sleep(1)
        self.motor.changeDirection()
        time_pool = 0
        real_delay = time.time()
        begin = time.time()
        while time_pool < 10:
            if self.flag == 0:
                self.motor.start()
                time.sleep(0.01)
                time_pool = time_pool + (time.time() - begin)
                begin = time.time()
            elif self.flag == 1:
                self.motor.stop()
                time.sleep(0.01)
                begin = time.time()


    def startService(self):
        super().startService()
        self.start()

    def detect(self):
        dis = 1000
        while True:
            time.sleep(0.2)
            dis = self.distanceDetector.getDistance()
            if dis < 5:
                self.flag = 1
                # if self.motor.getStatus() == self.motor.RUNNING:
                #     self.motor.pause()
            else :
                self.flag = 0

