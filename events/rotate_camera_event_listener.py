#!/usr/bin/env python

#-*- coding:utf-8 -*-

''
import logging

import config
import shared_data
from events.Listener import Listener
from sensors.servo import Servo

__author__ = 'PakhoLeung'

class RotateCameraEventListener(Listener):
    servo = None
    step = None
    direction = None

    def __init__(self) -> None:
        super().__init__()
        self.servo = Servo(config.CS_SERVO_CHANNEL)
        # 矫正摄像头位置
        self.servo.rotateTo(90)


    def excute(self, event):

        if 'step' in event.data:
            self.step = event.data['step']
        else :
            logging.error("haven't key 'step'. Terminate Excution")
            return

        if 'direction' in event.data:
            self.direction = event.data['direction']
        else :
            logging.error("haven't key 'direct'. Terminate Excution")
            return

        #开始旋转
        #若果向右，angle+，若果向左，angle-
        angle = 0
        if self.direction == 'left':
            if self.servo.presentAngle() - self.step < 0:
                angle = 0
            else :
                angle = self.servo.presentAngle() - self.step
        elif self.direction == 'right':
            if self.servo.presentAngle() - self.step > 180:
                angle = 180
            else :
                angle = self.servo.presentAngle() + self.step

        self.servo.rotateTo(angle)