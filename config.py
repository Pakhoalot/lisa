#!/usr/bin/env python

#-*- coding:utf-8 -*-

''
import logging
import RPi.GPIO as GPIO

__author__ = 'PakhoLeung'
#载入logging的设置
logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='lisa.log',
                        filemode='w')


console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

# 照片存放的位置
IMG_PATH = './captures/'
IMG_HEIGHT = 300
IMG_WIDTH = 400
# 每次照相的间隔，单位秒
CAPTURE_PERIOD = 30
# 摄像头预热时间，单位秒
PREVIEW_TIME = 0.5
# 矫正拍照间隔,最后一个是修正值
CAPTURE_PERIOD = CAPTURE_PERIOD - PREVIEW_TIME-0.88
# 普通传感器收集间隔
COLLECT_PERIOD = 1
# 上载图片的url
UPLOAD_IMG_URL = 'http://kylin.my/vinci/index.php/sensors/upload_img'

#定义GPIO模式
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)