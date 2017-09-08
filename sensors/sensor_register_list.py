#!/usr/bin/env python

#-*- coding:utf-8 -*-

''
import config
from sensors.camera import Camera
from sensors.liquid_level_sensor import LiquidLevelSensor
from sensors.switch import Switch

__author__ = 'PakhoLeung'

"""
这个表里注册了所有传感器，方便对传感器进行统一的管理
"""
CAMERA = Camera()
WD_INDICATOR = LiquidLevelSensor(channel=config.WDS_LIQUID_LEVEL_SENSOR_CHANNEL)
WD_PUMP = Switch(channel=config.WDS_PUMP_SWITCH_CHANNEL)
