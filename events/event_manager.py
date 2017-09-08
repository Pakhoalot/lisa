#!/usr/bin/env python

#-*- coding:utf-8 -*-

''
import logging
from queue import Queue, Empty
from threading import Thread

__author__ = 'PakhoLeung'

class EventManager:
    __eventQueue = Queue()
    __active = None #事件对象开关
    __thread = None
    __handlers = None
    def __init__(self) -> None:
        super().__init__()
        #初始化事件管理器
        #事件对象列表
        self.__eventQueue = Queue()
        self.active = False
        self.__thread = Thread(target=self.__run)
        # 这里的__handlers是一个字典，用来保存对应的事件的响应函数
        # 其中每个键对应的值是一个列表，列表中保存了对该事件监听的响应函数，一对多
        self.__handlers = {

        }


    def __eventProcess(self, event):
        #处理事件
        # 检查是否存在对该事件进行监听的处理函数
        if event.type in self.__handlers:
            #若存在，则按顺序将事件传递给处理函数执行
            for handler in self.__handlers[event.type]:
                handler(event)

    def __run(self):
        while self.__active == True:
            try:
                event = self.__eventQueue.get(block=True, timeout=1)
                self.__eventProcess(event)
            except Empty :
                pass

    def start(self):
        self.__active = True
        self.__thread.start()

    def stop(self):
        self.__active=False
        self.__thread.join()

    def addEventListener(self, type, handler):
        # 绑定事件和监听器处理函数
        try:
            handlerList = self.__handlers[type]
        except KeyError:
            handlerList = []

        self.__handlers[type] = handlerList
        #如果要注册的处理器不在该事件的处理器列表中，则注册事件
        if handler not in handlerList:
            handlerList.append(handler)

    def removeEventListener(self, type, handler):
        pass

    def sendEvent(self, event):
        self.__eventQueue.put(event)
