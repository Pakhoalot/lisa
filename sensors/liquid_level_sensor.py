#!/usr/bin/env python

#-*- coding:utf-8 -*-

''
import time

import config
from sensors.electronic_component import ElectronicComponent
import RPi.GPIO as GPIO

__author__ = 'PakhoLeung'

class LiquidLevelSensor(ElectronicComponent):
    __channel = None

    def __init__(self, channel) -> None:
        super().__init__()
        self.__channel = channel

    def getData(self):
        self.start()
        config.BUS.write_byte(config.ADDRESS, config.A0)
        value = config.BUS.read_byte(config.ADDRESS)
        print(value)
        self.stop()

    def terminate(self):
        super().terminate()

