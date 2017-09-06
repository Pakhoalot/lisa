#!/usr/bin/env python

#-*- coding:utf-8 -*-

''
from threading import Thread

import time

import config
from events.event import MyEvent
from sensors.pressure_sensor import PressureSensor
from sensors.servo import Servo

__author__ = 'PakhoLeung'




class FeedingEvent(MyEvent):
    servo = None
    pressureSensor = None
    present = None
    target = None

    def __init__(self, grams) -> None:
        super().__init__()
        servo = Servo(config.FE_SERVO_CHANNEL,
                      config.FE_SERVO_FREQUENT)
        self.pressureSensor = PressureSensor()
        self.target = grams
        self.present = self.pressureSensor.getData()

    def run(self):


        t = Thread(target=self.detect, args=(), daemon=True)
        t.start()

        if self.present < self.target:
            self.openGate()
        else:
            return
        while self.present < self.target:
            pass
        self.closeGate()
        #该线程终止
        t.join(timeout=0)


    def startEvent(self):
        self.run()


    def openGate(self):
        self.servo.rotateTo(90)

    def detect(self):
        while True:
            self.pressureSensor.getData()
            time.sleep(1)

    def closeGate(self):
        self.servo.rotateTo(0)