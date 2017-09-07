#!/usr/bin/env python

#-*- coding:utf-8 -*-

''

__author__ = 'PakhoLeung'
from sensors.electronic_component import ElectronicComponent

import logging

import time

import RPi.GPIO as GPIO

class Servo(ElectronicComponent):
    __channel = None
    __pwm = None
    __freq = None  # frequent
    __dc = None  # duty cycle
    __angle = None

    def __init__(self, channel: int, freq=50):
        super().__init__()
        self.__channel = channel
        self.__freq = freq
        self.angle = 0
        GPIO.setup(self.__channel, GPIO.OUT, initial=False)
        self.__pwm = GPIO.PWM(self.__channel, self.__freq)
        self.__pwm.start(0)


    def start(self):
        super().start()
        self.__pwm.start(0)

    def terminate(self):
        super().terminate()
        GPIO.output(self.__channel, GPIO.LOW)
        GPIO.cleanup(self.__channel)

    def pause(self):
        super().pause()
        GPIO.output(self.__channel, GPIO.LOW)

    def changeFrequency(self, freq):
        self.__freq = freq
        self.__pwm.ChangeFrequency(self.__freq)

    def __changeDC(self, dc):
        self.__dc = dc
        self.__pwm.ChangeDutyCycle(self.__dc)

    def stop(self):
        super().stop()
        self.__pwm.stop()

    def rotateTo(self, angle):
        # 该函数传入一个角度制角度，为舵机旋转一定角度
        # 这是一个耗时函数，请不要在主函数使用该函数
        if angle < 0 or angle > 180:
            raise ValueError("Angle is out of Bound.")
        # if threading.current_thread() == threading._main_thread:
        #     raise threading.ThreadError("spin is a time-consuming job. Can't run in mainThread.")
        if self.getStatus() == self.RUNNING:
            logging.info("This servo is occupied.")
            return
        self.start()
        self.__dc = (angle / (180 - 0)) * (12.5 - 2.5) + 2.5
        self.__changeDC(self.__dc)
        self.__angle = angle
        time.sleep(1)
        self.stop()

    def presentAngle(self):
        return self.__angle