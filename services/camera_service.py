#!/usr/bin/env python

#-*- coding:utf-8 -*-

''
import time

import config
import upload_data
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
            #得到路径，为未来的上传准备
            img_path = self.camera.capture()
            upload_data.IMG_PATH = img_path
            time.sleep(config.CAPTURE_PERIOD)


