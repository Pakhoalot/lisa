#!/usr/bin/env python

#-*- coding:utf-8 -*-

''
import logging
import threading
import time

import config
import upload_data
from sensors.camera import Camera
from services.service import Service

__author__ = 'PakhoLeung'

class CameraService(Service,threading.Thread):
    camera = None

    def __init__(self) -> None:
        super().__init__()
        self.camera = Camera()

    def run(self):
        while True:
            t = time.time()
            #得到路径，为未来的上传准备
            img_path = self.camera.capture()
            upload_data.IMG_PATH = img_path
            logging.info("newest uplodad_img change to"+ upload_data.IMG_PATH)
            time.sleep(config.CAPTURE_PERIOD)
            period = time.time()-t
            logging.debug("camera service lasts "+str(period))

    def startService(self):
        self.start()


