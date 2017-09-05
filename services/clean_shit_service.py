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

        #尝试使用手动步进
        i = 0
        while i < 370:
            if self.flag == 0:
                self.motor.setDirection(self.motor.LEFT)
                self.motor.forward()
                i = i+1
            elif self.flag == 1:
                self.motor.setDirection(self.motor.RIGHT)
                self.motor.forward()
                i = i-1
                pass

    def startService(self):
        super().startService()
        self.start()

    def detect(self):
        dis = 1000
        while True:
            time.sleep(0.2)
            dis = self.distanceDetector.getDistance()
            if dis > 100:
                continue
            print(dis)
            if dis < 50:
                self.flag = 1
                # if self.motor.getStatus() == self.motor.RUNNING:
                #     self.motor.pause()
            else :
                self.flag = 0

