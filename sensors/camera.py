#!/usr/bin/env python

#-*- coding:utf-8 -*-

''
import logging
import threading

from sensors.electronic_component import ElectronicComponent

import picamera
import time
import config

__author__ = 'PakhoLeung'

class Camera(ElectronicComponent):
    def __init__(self) -> None:
        super().__init__()

    def capture(self):
        if threading.current_thread() == threading._main_thread:
            raise threading.ThreadError("capture is a time-consuming job. Can't run in mainThread.")
        #判断状态
        status = self.getStatus()
        if status == self.TERMINATED:
            logging.info("this camera had been terminated.")
            return None
        if status == self.IDLE:
            self.setStatus(self.RUNNING)
        with picamera.PiCamera() as camera:
            camera.resolution = (config.IMG_WIDTH, config.IMG_HEIGHT)
            camera.start_preview()
            # 摄像头预热
            logging.info('camera prepare')
            time.sleep(config.PREVIEW_TIME)
            t = str(int(time.time()))
            file_path = config.IMG_PATH + t + '.jpg'
            camera.capture(file_path)
            logging.info('capture ' + file_path)
            return file_path
        self.setStatus(self.IDLE)