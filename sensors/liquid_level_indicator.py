#!/usr/bin/env python

#-*- coding:utf-8 -*-

''
from sensors.electronic_component import ElectronicComponent
import RPi.GPIO as GPIO

__author__ = 'PakhoLeung'

class LiquidLevelIndicator(ElectronicComponent):
    __channel = None
    def __init__(self, channel) -> None:
        super().__init__()
        self.__channel = channel
        GPIO.setup(self.__channel, GPIO.IN)

    def getData(self):
        return GPIO.input(self.__channel)

    def terminate(self):
        super().terminate()
        GPIO.cleanup(self.__channel)

