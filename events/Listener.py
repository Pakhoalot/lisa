#!/usr/bin/env python

#-*- coding:utf-8 -*-

''

__author__ = 'PakhoLeung'

class Listener():
    def __init__(self) -> None:
        super().__init__()

    def excute(self,event):
        raise NotImplementedError