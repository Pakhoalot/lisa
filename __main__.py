#!/usr/bin/env python

#-*- coding:utf-8 -*-

''
import logging

from services.camera_service import CameraService
from services.water_dispenser_service import WaterDispenserService

__author__ = 'PakhoLeung'

import time
import threading
import RPi.GPIO as GPIO
import config

if __name__ == '__main__':

    try:
        cameraService = CameraService()
        cameraService.startService()
        waterSercice = WaterDispenserService(channel=7)
        waterSercice.startService()
    except KeyboardInterrupt:
        pass