#!/usr/bin/env python

#-*- coding:utf-8 -*-

''

__author__ = 'PakhoLeung'

class MyEvent:
    type = None
    data = {}
    def __init__(self,type, data=None) -> None:
        super().__init__()
        self.type = type
        self.data.update(data)

    def addData(self, data):
        self.data.update(data)
