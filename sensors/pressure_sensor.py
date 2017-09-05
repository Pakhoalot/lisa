#!/usr/bin/env python

#-*- coding:utf-8 -*-

''
from sensors.electronic_component import ElectronicComponent
import RPi.GPIO as GPIO

__author__ = 'PakhoLeung'


class PressureSensor(ElectronicComponent):
    def __init__(self) -> None:
        super().__init__()