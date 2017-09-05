#!/usr/bin/env python

#-*- coding:utf-8 -*-

''
import RPi.GPIO as GPIO
import time

__author__ = 'PakhoLeung'

class DistanceDetector():
    __trigger = None
    __echo = None
    def __init__(self, trig, echo) -> None:
        super().__init__()
        self.__echo = echo
        self.__trigger = trig
        GPIO.setup(self.__trigger, GPIO.OUT)
        GPIO.setup(self.__echo, GPIO.IN)


    def getDistance(self):
        # 发出一段10us的脉冲
        GPIO.output(self.__trigger, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(self.__trigger, GPIO.LOW)

        while GPIO.input(self.__echo) == 0:
            pass
        pulse_start = time.time()

        #等待高电平结束
        while GPIO.input(self.__echo) == 1 and time.time()-pulse_start < 0.01:
            pass
        pulse_end = time.time()
        pulse_duration = pulse_end-pulse_start
        distance = pulse_duration * 17150
        distance = round(distance,2)
        return distance


