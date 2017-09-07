#!/usr/bin/env python

#-*- coding:utf-8 -*-

''
import logging

from events.clean_shit_event_listener import CleanShitEventListener
from events.event_manager import EventManager
from events.event_register_list import *
from events.feeding_event_listener import FeedingEventListener
from events.myevent import MyEvent
from sensors.distance_detector import DistanceDetector
from sensors.pressure_sensor import PressureSensor
from sensors.servo import Servo
from services.camera_service import CameraService
from services.clean_shit_service import CleanShitService
from services.water_dispenser_service import WaterDispenserService
import time
import threading
import RPi.GPIO as GPIO
import config

__author__ = 'PakhoLeung'


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


        # 测试超声波距离传感器
        # dd = DistanceDetector(7,8)
        # while True:
        #     time.sleep(0.2)
        #     dis = dd.getDistance()
        #     print(dis)

        # 尝试使用事件驱动模型
        eventManager = EventManager()
        feedingEventListener = FeedingEventListener()
        cleanShitEventListener = CleanShitEventListener()
        eventManager.addEventListener(EVENT_FEEDING,feedingEventListener.excute)
        eventManager.addEventListener(EVENT_CLEAN_SHIT, cleanShitEventListener.excute)

        eventManager.start()

        while True:
            logging.info("start")
            input("haha:")
            eventManager.sendEvent(event=MyEvent(
                type=EVENT_FEEDING,
                data={
                    'target': 280
                }))


        #测试压力传感器
        # pressureSensor = PressureSensor(SCK_channel=7, DT_channel=8)
        # while True:
        #     print(pressureSensor.getData())
        #     time.sleep(1)

    except KeyboardInterrupt:
        pass