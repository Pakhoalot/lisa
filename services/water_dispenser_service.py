#!/usr/bin/env python

#-*- coding:utf-8 -*-

''
import logging
import time
from threading import Thread

import requests

import config
from sensors.liquid_level_sensor import LiquidLevelSensor
from sensors.switch import Switch
from services.service import Service

__author__ = 'PakhoLeung'

class WaterDispenserService(Service):
    indicator = None
    pump = None

    def __init__(self) -> None:
        super().__init__()
        self.indicator = LiquidLevelSensor(channel=config.WDS_LIQUID_LEVEL_SENSOR_CHANNEL)
        self.pump = Switch(channel=config.WDS_PUMP_SWITCH_CHANNEL)

    def run(self):
        uploadThread = Thread(target=self.__uploadLoop, args=(), daemon=True)
        uploadThread.start()

        self.pump.on()
        while True:
            level = self.indicator.getData()
            if level == 0 and self.pump.getStatus() == self.pump.RUNNING:
                logging.info("liquid level is 0, pump stops")
                self.pump.off()
            elif level!=0 and self.pump.getStatus() == self.pump.IDLE:
                self.pump.on()
            # self.shareData("LIQUID_LEVEL", level)
            logging.debug("the liquid level is "+str(level))
            time.sleep(2)

    def startService(self):
        self.start()


    def stopService(self):
        pass


    def __upload(self, liquid_level):
        sensorId = 3
        data = {
            'type': 'value',
            'value': liquid_level
        }
        url = config.UPLOAD_URL+config.USER_ID+'/'+config.DEVICE_ID+'/'+ str(sensorId)
        response = requests.post(url=url, data=data)
        return response

    def __uploadLoop(self):
        while True:
            liquid_level = self.indicator.getData()
            self.__upload(liquid_level=liquid_level)
            time.sleep(config.WDS_UPLOAD_FREQUENT)



