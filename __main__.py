#!/usr/bin/env python

#-*- coding:utf-8 -*-

''
import logging

from services.camera_service import CameraService

__author__ = 'PakhoLeung'

import time
import threading
import RPi.GPIO as GPIO
import config

if __name__ == '__main__':

    try:
        cameraService = CameraService()
        t1 = threading.Thread(target=cameraService.startService,args=())
        t1.start()
    except KeyboardInterrupt:
        logging.info("main ends")