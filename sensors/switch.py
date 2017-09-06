#!/usr/bin/env python

#-*- coding:utf-8 -*-

''
import RPi.GPIO as GPIO
from sensors.electronic_component import ElectronicComponent

__author__ = 'PakhoLeung'

class Switch(ElectronicComponent):
    __channel = None
    def __init__(self,channel) -> None:
        super().__init__()
        self.__channel = channel
        GPIO.setup(self.__channel,GPIO.OUT)
        self.off()


    def on(self):
        self.start()
        GPIO.output(self.__channel, GPIO.HIGH)

    def off(self):
        self.stop()
        GPIO.output(self.__channel, GPIO.LOW)

