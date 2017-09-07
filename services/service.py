#!/usr/bin/env python
#-*- coding:utf-8 -*-

''
from multiprocessing import Process

import shared_data

__author__ = 'PakhoLeung'

#Servcice 基类只是用来表示这是一个Service
class Service(Process):
    def __init__(self) -> None:
        super().__init__()

    def startService(self):
        raise NotImplementedError

    def stopService(self):
        raise NotImplementedError

    def shareData(self, key:str, value):
        shared_data.update_data(key, value)
