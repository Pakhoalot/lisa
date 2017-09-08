#!/usr/bin/env python

#-*- coding:utf-8 -*-

''
from sensors.electronic_component import ElectronicComponent
import RPi.GPIO as GPIO
import time
__author__ = 'PakhoLeung'


class PressureSensor(ElectronicComponent):
    __DT = None
    __SCK = None
    def __init__(self, SCK_channel, DT_channel) -> None:
        super().__init__()
        self.__DT = DT_channel
        self.__SCK = SCK_channel
        GPIO.setup(self.__SCK, GPIO.OUT)
        GPIO.setup(self.__DT, GPIO.IN)
        GPIO.output(self.__SCK, GPIO.LOW)


    def getData(self):
        value = 0
        GPIO.setup(self.__DT, GPIO.OUT)
        GPIO.output(self.__DT, GPIO.HIGH)
        GPIO.setup(self.__DT, GPIO.IN)
        GPIO.output(self.__SCK, GPIO.LOW)

        while GPIO.input(self.__DT) == GPIO.LOW:
            pass
        time.sleep(0.000001)

        for i in range(1, 25):
            GPIO.output(self.__SCK, GPIO.HIGH)
            value = value << 1
            time.sleep(0.000001)
            GPIO.output(self.__SCK, GPIO.LOW)
            if GPIO.input(self.__DT) == GPIO.HIGH:
                value = value + 1
            time.sleep(0.000002)

        GPIO.output(self.__SCK, GPIO.HIGH)
        time.sleep(0.000002)
        GPIO.output(self.__SCK, GPIO.LOW)
        time.sleep(0.000002)

        return value