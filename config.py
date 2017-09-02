#!/usr/bin/env python

#-*- coding:utf-8 -*-

''

__author__ = 'PakhoLeung'
# 照片存放的位置
IMG_PATH = './capture/'
IMG_HEIGHT = 300
IMG_WIDTH = 400
# 每次照相的间隔，单位秒
CAPTURE_PERIOD = 30
# 摄像头预热时间，单位秒
PREVIEW_TIME = 0.5
# 矫正拍照间隔
CAPTURE_PERIOD = CAPTURE_PERIOD - PREVIEW_TIME
# 普通传感器收集间隔
COLLECT_PERIOD = 1
# 上载图片的url
UPLOAD_IMG_URL = 'http://kylin.my/vinci/index.php/sensors/upload_img'