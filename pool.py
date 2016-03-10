# -*- coding:utf-8 -*-

import exchanger

class ThreadPool:
    def __init__(self):
        self.threads = []
        self.queues = []
        self.host = '127.0.0.1'
        self.post = 5672
        self.username = 'guest'
        self.password = 'guest'

    def new(self, channelType, channelName):
        queue = exchanger.InternalQueue()
        self.queues.append(queue)

        if channelType == "publish":
            threadDemo = exchanger.Publisher(self.host,
                                             self.port,
                                             self.username,
                                             self.password,
                                             channelName,
                                             queue)
            threadDemo.start()
            self.threads.append(threadDemo)
        if channelType == "subscribe":
            threadDemo = exchanger.Consumer(self.host,
                                            self.port,
                                            self.username,
                                            self.password,
                                            channelName,
                                            queue)
            threadDemo.start()
            self.threads.append(threadDemo)

    def clear(self):
        while len(self.threads) != 0:
            threadDemo = self.threads.pop()
            threadDemo.stop()
