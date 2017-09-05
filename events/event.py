#!/usr/bin/env python

#-*- coding:utf-8 -*-

''

__author__ = 'PakhoLeung'

class MyEvent:
    def __init__(self) -> None:
        super().__init__()

    def startEvent(self):
        raise NotImplementedError
