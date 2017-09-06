#!/usr/bin/env python

#-*- coding:utf-8 -*-

''
import logging

from sensors.distance_detector import DistanceDetector
from sensors.pressure_sensor import PressureSensor
from sensors.servo import Servo
from services.camera_service import CameraService
from services.clean_shit_service import CleanShitService
from services.water_dispenser_service import WaterDispenserService

__author__ = 'PakhoLeung'

import time
import threading
import RPi.GPIO as GPIO
import config

if __name__ == '__main__':



    try:
        # cameraService = CameraService()
        # cameraService.startService()
        # waterSercice = WaterDispenserService(channel=7)
        # waterSercice.startService()
        # cleanService = CleanShitService()
        # cleanService.startService()

        # servo = Servo(channel=11,freq=50)
        # while True:
        #     servo.rotate(0)
        #     time.sleep(1)
        #     servo.rotate(180)
        #     time.sleep(1)


        #test distance
        # dd = DistanceDetector(7,8)
        # while True:
        #     time.sleep(0.2)
        #     dis = dd.getDistance()
        #     print(dis)


        pass

    except KeyboardInterrupt:
        pass