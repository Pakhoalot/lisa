#!/usr/bin/env python

#-*- coding:utf-8 -*-

''
from sensors.electronic_component import ElectronicComponent

__author__ = 'PakhoLeung'

class Switch(ElectronicComponent):
    __channel = None
    def __init__(self,channel) -> None:
        super().__init__()
        self.__channel = channel


    def on(self):
        pass

    def off(self):
        pass

