#!/usr/bin/env python

#-*- coding:utf-8 -*-

''
import logging
import time

import requests

import config
from sensors.camera import Camera
from services.service import Service

__author__ = 'PakhoLeung'

class CameraService(Service):
    camera = None
    img_path = None


    def __init__(self) -> None:
        super().__init__()
        self.camera = Camera()

    def run(self):
        while True:
            t = time.time()
            #得到路径，为未来的上传准备
            self.img_path = self.camera.capture()
            # self.shareData("IMG_PATH", self.img_path)
            self.__upload(img_path=self.img_path)
            logging.debug("newest uplodad_img change to"+ self.img_path)
            time.sleep(config.CAPTURE_PERIOD)


    def startService(self):
        self.start()

    def stopService(self):
        pass

    def __upload(self, img_path):
        sensorId = 2
        data = {
            'type': 'img'
        }
        files = {
            'img': open(img_path, 'rb')
        }
        url = config.UPLOAD_URL+config.USER_ID+'/'+config.DEVICE_ID+'/'+ str(sensorId)
        response = requests.post(url=url, data=data, files=files)
        return response