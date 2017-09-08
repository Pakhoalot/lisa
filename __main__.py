#!/usr/bin/env python

#-*- coding:utf-8 -*-

''
import logging

import time

from events.clean_shit_event_listener import CleanShitEventListener
from events.event_manager import EventManager
from events.event_register_list import *
from events.feeding_event_listener import FeedingEventListener
from events.myevent import MyEvent
from events.rotate_camera_event_listener import RotateCameraEventListener
from sensors.pressure_sensor import PressureSensor

__author__ = 'PakhoLeung'


def waitForEvent():
    #抽象等待并接受数据的方法，打包并返回一个event对象
    type = input('input type:')
    data = {}
    key = ''
    value = 0
    while True:
        key = input('input key:')
        if key == 'end':
            break
        value = input('input value:')
        data[key] = value

    event = MyEvent(type=type, data=data)
    return event

    pass

def main():
    try:

        # 测试伺服机
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

        #测试压力传感器
        # pressureSensor = PressureSensor(SCK_channel=7, DT_channel=8)
        # while True:
        #     print(pressureSensor.getData())
        #     time.sleep(1)


        #开启服务
        # cameraService = CameraService()
        # cameraService.startService()
        # waterSercice = WaterDispenserService(channel=7)
        # waterSercice.startService()
        # cleanService = CleanShitService()
        # cleanService.startService()

        # 尝试使用事件驱动模型
        eventManager = EventManager()
        feedingEventListener = FeedingEventListener()
        # cleanShitEventListener = CleanShitEventListener()
        rotateCameraEventListener = RotateCameraEventListener()
        eventManager.addEventListener(EVENT_FEEDING,feedingEventListener.excute)
        # eventManager.addEventListener(EVENT_CLEAN_SHIT, cleanShitEventListener.excute)
        eventManager.addEventListener(EVENT_ROTATE_CAMERA, rotateCameraEventListener.excute)

        eventManager.start()

        while True:
            logging.info("start")
            event = waitForEvent()
            eventManager.sendEvent(event)
            print(event.data.items())


    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()


