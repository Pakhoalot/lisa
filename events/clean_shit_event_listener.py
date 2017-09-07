#!/usr/bin/env python

#-*- coding:utf-8 -*-

''
from events.Listener import Listener
import logging
import threading
import time
import config
from sensors.distance_detector import DistanceDetector
from sensors.motor_hand_made import Motor
from sensors.switch import Switch

__author__ = 'PakhoLeung'

class CleanShitEventListener(Listener):
    __TAIL = 360
    __HEAD = 0
    __POSITION = None
    motor = None
    distanceDetector = None
    switch = None
    def __init__(self) -> None:
        super().__init__()
        self.motor = Motor(config.CSS_MOTOR_PWM_CHANNEL,
                           config.CSS_MOTOR_DIR_CHANNEL,
                           config.CSS_MOTOR_ENABLED_CHANNEL,
                           config.CSS_MOTOR_FREQUENT)
        self.distanceDetector = DistanceDetector(config.CSS_DD_TRIGER_CHANNEL,
                                                 config.CSS_DD_ECHO_CHANNEL)
        self.switch = Switch(config.CSS_SWITCH_CHANNEL)
        # 设置版位置为零
        self.__POSITION = 0


    def excute(self, event):
        # 开启距离实时监测
        t1 = threading.Thread(target=self.detect, args=(), daemon=True)
        t1.start()
        # 尝试使用switch
        self.switch.on()
        time.sleep(2)

        # 板复位
        self.moveToHead()

        while self.__POSITION < self.__TAIL:
            logging.info("start forward")
            if self.flag == 0:
                logging.info(self.__POSITION)
                self.motor.setDirection(self.motor.RIGHT)
                self.motor.forward()
                self.__POSITION = self.__POSITION + 1
            elif self.flag == 1:
                logging.info("Cleaner is blocked. Reset and preapre to Restart")
                self.moveToHead()
                # 当前方没物体时，重启机器
                while self.flag == 1:
                    time.sleep(3)
                    pass
                time.sleep(5)
                logging.info("Clear. Begin to restart")

        logging.info("Clean up.")
        time.sleep(3)
        self.moveToHead()

        # 尝试使用继电器关闭
        self.switch.off()
        time.sleep(2)
        t1.join(timeout=0)

    def moveToHead(self):
        if self.__POSITION != self.__HEAD:
            self.motor.setDirection(self.motor.LEFT)
            while self.__POSITION != 0:
                logging.info(self.__POSITION)
                self.motor.forward()
                self.__POSITION = self.__POSITION - 1

    def moveToTail(self):
        if self.__POSITION != self.__TAIL:
            self.motor.setDirection(self.motor.RIGHT)
            while self.__POSITION != 0:
                logging.info(self.__POSITION)
                self.motor.forward()
                self.__POSITION = self.__POSITION - 1


    def detect(self):
        while True:
            time.sleep(0.5)
            dis = self.distanceDetector.getDistance()
            if dis < 50:
                self.flag = 1
                # if self.motor.getStatus() == self.motor.RUNNING:
                #     self.motor.pause()
            else:
                self.flag = 0


