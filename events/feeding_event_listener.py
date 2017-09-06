#!/usr/bin/env python

#-*- coding:utf-8 -*-

''
import logging
import threading
from threading import Thread
import time
import config
from events.Listener import Listener
from sensors.pressure_sensor import PressureSensor
from sensors.servo import Servo

__author__ = 'PakhoLeung'




class FeedingEventListener(Listener):
    servo = None
    pressureSensor = None
    target = None
    present = None

    def __init__(self) -> None:
        super().__init__()
        self.servo = Servo(config.FE_SERVO_CHANNEL,
                      config.FE_SERVO_FREQUENT)
        self.pressureSensor = PressureSensor()
        self.present = self.pressureSensor.getData()


    def excute(self, event):
        # Listener的执行方法，注册时使用的方法
        if 'target' in event.data:
            self.target = event.data['target']
        else :
            logging.error("haven't key 'target'. Terminate Excution")
            return

        t = Thread(target=self.detect, args=(), daemon=True)
        t.start()

        if self.present < self.target:
            logging.info("in "+ threading.current_thread().getName()+": "+"open the gate!")
            self.openGate()
        else:
            return
        while self.present < self.target:
            # self.dectect()
            pass
        self.closeGate()
        #该线程终止
        t.join(timeout=0)



    def openGate(self):
        self.servo.rotateTo(90)

    def detect(self):
        while True:
            self.pressureSensor.getData()
            time.sleep(1)

    def closeGate(self):
        self.servo.rotateTo(0)