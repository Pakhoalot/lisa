#!/usr/bin/env python

#-*- coding:utf-8 -*-

''
from sensors.camera import Camera
from services.service import Service

__author__ = 'PakhoLeung'

class CameraService(Service):
    camera = None

    def __init__(self) -> None:
        super().__init__()
        self.camera = Camera()

    def startService(self):
        while True:
            camera.capture()


