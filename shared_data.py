#!/usr/bin/env python

#-*- coding:utf-8 -*-

''

__author__ = 'PakhoLeung'

data = {

}

def update_data(key, value):
    data[key] = value

def update_dict(dict):
    data.update(dict)

def getData(key):
    data.get(key)