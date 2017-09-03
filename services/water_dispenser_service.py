#!/usr/bin/env python

#-*- coding:utf-8 -*-

''
import logging
from threading import Thread

import time

import upload_data
from sensors.liquid_level_indicator import LiquidLevelIndicator
from sensors.switch import Switch
from services.service import Service

__author__ = 'PakhoLeung'

class WaterDispenserService(Service,Thread):
    indicator = None
    pump = None

    def __init__(self, channel) -> None:
        super().__init__()
        self.indicator = LiquidLevelIndicator(channel=channel)
        self.pump = Switch()


    def run(self):
        self.pump.start()
        while True:
            level = self.indicator.getData()
            if level == 0 and self.pump.getStatus() == self.pump.RUNNING:
                logging.info("liquid level is 0, pump stops")
                self.pump.stop()
            elif level!=0 and self.pump.getStatus() == self.pump.IDLE:
                self.pump.start()
            upload_data.LIQUID_LEVEL = level
            logging.info("the liquid level is "+str(level))
            time.sleep(0.5)

    def startService(self):
        self.start()





