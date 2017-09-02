#!/usr/bin/env python

#-*- coding:utf-8 -*-

''

__author__ = 'PakhoLeung'

class ElectronicComponent:
    __status = None
    IDLE = 1
    RUNNING = 2
    PAUSE = 3
    TERMINATED = 4

    def __init__(self) -> None:
        super().__init__()
        self.setStatus(self.IDLE)

    def getStatus(self):
        return self.__status

    def setStatus(self, status):
        self.status = status

    def start(self):
        self.setStatus(self.RUNNING)

    def terminate(self):
        self.setStatus(self.TERMINATED)


    def pause(self):
        self.setStatus(self.PAUSE)
