#!/usr/bin/env python

#-*- coding:utf-8 -*-

''
from sensors.electronic_component import ElectronicComponent
import RPi.GPIO as GPIO
import smbus
import time
__author__ = 'PakhoLeung'


class PressureSensor(ElectronicComponent):
    def __init__(self) -> None:
        super().__init__()


    def getData(self):
        pass