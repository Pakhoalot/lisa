#!/usr/bin/env python
#-*- coding:utf-8 -*-

''
__author__ = 'PakhoLeung'

#Servcice 基类只是用来表示这是一个Service
class Service:
    def __init__(self) -> None:
        super().__init__()

    def startService(self):
        raise NotImplementedError

    def stopService(self):
        raise NotImplementedError