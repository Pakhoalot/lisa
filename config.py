#!/usr/bin/env python

#-*- coding:utf-8 -*-

''
import logging
import RPi.GPIO as GPIO
import smbus

__author__ = 'PakhoLeung'
#载入logging的设置
logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(process)d %(threadName)s %(message)s ',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='lisa.log',
                        filemode='a')


console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(name)s: %(levelname)s: %(process)d: %(threadName)s: %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

#定义GPIO模式
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)


#i2c接口地址定义
ADDRESS = 0x48
A0 = 0x40
A1 = 0x41
A2 = 0x42
A3 = 0x43
BUS = smbus.SMBus(1)

#定义用户id和设备id
USER_ID = 1
DEVICE_ID = 1
#定义网络上传地址和网址根目录
WEBSITE_ROOT = 'http://kylin.my/vinci/index.php/'
#上载数据事例
#post(data) url=http://kylin.my/vinci/index.php/api/<user_id>/<device_id>/<sensor_id>
# 上载图片的url
UPLOAD_URL = 'http://kylin.my/vinci/index.php/api/'


#相机模块 定义
# 照片存放的位置
IMG_PATH = './captures/'
IMG_HEIGHT = 300
IMG_WIDTH = 400
# 每次照相的间隔，单位秒
CAPTURE_PERIOD = 10
# 摄像头预热时间，单位秒
PREVIEW_TIME = 0.5
# 矫正拍照间隔,最后一个是修正值
CAPTURE_PERIOD = CAPTURE_PERIOD - PREVIEW_TIME - 0.88
CS_SERVO_CHANNEL = 11

#扫屎模块 电机针脚定义
CSS_MOTOR_PWM_CHANNEL = 3
CSS_MOTOR_DIR_CHANNEL = 5
CSS_MOTOR_ENABLED_CHANNEL = 11
CSS_MOTOR_FREQUENT = 50000
CSS_SWITCH_CHANNEL = 11
#超声波传感器 针脚定义
CSS_DD_TRIGER_CHANNEL = 7
CSS_DD_ECHO_CHANNEL = 8

#喂食模块 针脚定义
FE_SERVO_CHANNEL = 12
FE_SERVO_FREQUENT = 50
#压力传感器 针脚定义
FE_PRESSURE_SCK_CHANNEL = 7
FE_PRESSURE_DT_CHANNEL = 8
#饮水机模块 针脚定义
WDS_LIQUID_LEVEL_SENSOR_CHANNEL = A0
WDS_PUMP_SWITCH_CHANNEL = 14
WDS_UPLOAD_FREQUENT = 30*60