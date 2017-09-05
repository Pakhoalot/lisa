#!/usr/bin/env python

#-*- coding:utf-8 -*-

''

__author__ = 'PakhoLeung'

#!/usr/bin/env python

#-*- coding:utf-8 -*-

''

import threading
import time
import RPi.GPIO as GPIO

from sensors.electronic_component import ElectronicComponent

__author__ = 'PakhoLeung'

class Motor(ElectronicComponent):

    __channel1 = None  # PWM信号
    __channel2 = None  # 方向信号
    __channel3 = None  # 使能信号
    LEFT = 5
    RIGHT = 6
    __freq = None
    direction = None

    def __init__(self, PWM_channel:int, dir_channel: int, enabled_channel: int, freq) -> None:
        super().__init__()
        # channel1 给PWM信号
        self.__channel1 = PWM_channel
        self.__freq = freq
        GPIO.setup(self.__channel1, GPIO.OUT)

        # channel2 给方向信号
        self.__channel2 = dir_channel
        self.direction = self.LEFT
        GPIO.setup(self.__channel2, GPIO.OUT)
        # GPIO.output(self.__channel2, GPIO.HIGH)

        # channel3 给使能信号，初始为LOW
        self.__channel3 = enabled_channel
        GPIO.setup(self.__channel3, GPIO.OUT)
        GPIO.output(self.__channel3, GPIO.LOW)

    #返回三只信号脚，分别对应PWM，方向，和使能
    def getChannel(self):
        return [self.__channel1, self.__channel2, self.__channel3]

    #获取电机方向
    def getDirection(self):
        return self.direction

    # 改变电机方向
    def changeDirection(self):
        if self.direction == self.LEFT:
            self.direction = self.RIGHT
            GPIO.cleanup(self.__channel2)
        elif self.direction == self.RIGHT:
            self.direction = self.LEFT
            GPIO.setup(self.__channel2, GPIO.OUT)
            GPIO.output(self.__channel2, GPIO.LOW)

        return self.direction

    def setDirection(self, direction):
        if self.direction == self.LEFT and self.direction != direction:
            self.direction = self.RIGHT
            GPIO.cleanup(self.__channel2)
            time.sleep(0.5)
        elif self.direction == self.RIGHT and self.direction != direction:
            self.direction = self.LEFT
            GPIO.setup(self.__channel2, GPIO.OUT)
            GPIO.output(self.__channel2, GPIO.LOW)
            time.sleep(0.5)
    #令点击开始转动
    def start(self):
        super().start()
        GPIO.output(self.__channel3, GPIO.LOW)

    def pause(self):
        super().pause()
        GPIO.output(self.__channel3, GPIO.HIGH)


    def stop(self):
        super().stop()
        GPIO.output(self.__channel3,GPIO.HIGH)

    def terminate(self):
        super().terminate()
        GPIO.output(self.__channel3, GPIO.LOW)
        channel = [self.__channel1, self.__channel2, self.__channel3]
        GPIO.cleanup(channel)

    def forward(self):
        for i in range(1,101):
            GPIO.output(self.__channel1, GPIO.LOW)
            time.sleep(0.00005)
            GPIO.output(self.__channel1, GPIO.HIGH)
            time.sleep(0.00005)



if __name__ == '__main__':
    GPIO.cleanup()
    GPIO.setmode(GPIO.BOARD)
    PWMchannel = 8
    dirchannel = 7
    motor = Motor(PWM_channel=PWMchannel, dir_channel=dirchannel, enabled_channel=10,freq=50000)
    motor.start()
    # motor.terminate()
    # GPIO.setup(8,GPIO.OUT)
    print("it is running")
    # while True:
    #     GPIO.output(8,GPIO.LOW)
    #     time.sleep(0.1)
    #     GPIO.output(8,GPIO.HIGH)
    #     time.sleep(0.1)
    # GPIO.setup(8, GPIO.OUT, initial=False)
    # pwm = GPIO.PWM(8, 500)
    # pwm.start(50)
    while True:
        time.sleep(5)
        motor.pause()
        print(motor.changeDirection())
        time.sleep(5)
        motor.start()