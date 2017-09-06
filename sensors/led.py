#!/usr/bin/env python

#-*- coding:utf-8 -*-

''

__author__ = 'PakhoLeung'
import logging

from sensors.electronic_component import ElectronicComponent

import asyncio

import time

import RPi.GPIO as GPIO


class LED(ElectronicComponent):
    __channel = None
    __delay = None

    def __init__(self, channel:int, delay=2) -> None:
        super().__init__()
        self.__channel = channel
        GPIO.setup(self.__channel, GPIO.OUT)

    def start(self):
        super().start()

    def terminate(self):
        super().terminate()
        GPIO.output(self.__channel, GPIO.LOW)
        GPIO.cleanup(self.__channel)

    def pause(self):
        super().pause()
        GPIO.output(self.__channel, GPIO.LOW)

    def lightup(self):
        if self.getStatus() != self.IDLE:
            logging.warning("This led is used or had been terminated.")
            return None
        GPIO.output(self.__channel,GPIO.LOW)

    def lightoff(self):
        if self.getStatus() != self.IDLE:
            logging.warning("This led is used or had been terminated.")
        GPIO.output(self.__channel, GPIO.HIGH)