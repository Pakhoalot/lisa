#!/usr/bin/env python

#-*- coding:utf-8 -*-

''
import config
from events.event import MyEvent
from sensors.servo import Servo

__author__ = 'PakhoLeung'




class FeedingEvent(MyEvent):
    servo = None
    pressureSensor = None
    def __init__(self) -> None:
        super().__init__()
        servo = Servo(config.FE_SERVO_CHANNEL,
                      config.FE_SERVO_FREQUENT)
        pressureSensor = PressureSensor()
    def run(self):
        self.openGate()

    def startEvent(self):
        self.run()

    def openGate(self):
        self.servo.rotate(90)
        pass
