#!/usr/bin/env python

#-*- coding:utf-8 -*-

''
import logging
from threading import Thread
import time
import config
from sensors.liquid_level_sensor import LiquidLevelSensor
from sensors.switch import Switch
from services.service import Service

__author__ = 'PakhoLeung'

class WaterDispenserService(Service,Thread):
    indicator = None
    pump = None

    def __init__(self) -> None:
        super().__init__()
        self.indicator = LiquidLevelSensor(channel=config.WDS_LIQUID_LEVEL_SENSOR_CHANNEL)
        self.pump = Switch(channel=config.WDS_PUMP_SWITCH_CHANNEL)


    def run(self):
        self.pump.on()
        while True:
            level = self.indicator.getData()
            if level == 0 and self.pump.getStatus() == self.pump.RUNNING:
                logging.info("liquid level is 0, pump stops")
                self.pump.off()
            elif level!=0 and self.pump.getStatus() == self.pump.IDLE:
                self.pump.on()
            self.shareData("LIQUID_LEVEL", level)
            logging.info("the liquid level is "+str(level))
            time.sleep(2)

    def startService(self):
        self.start()





