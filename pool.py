# -*- coding:utf-8 -*-

import exchanger

class ThreadPool:
    def __init__(self):
        self.threads = []
        self.queues = []
        self.hashes = dict()
        self.host = '127.0.0.1'
        self.post = 5672
        self.username = 'guest'
        self.password = 'guest'

    def new(self, channelType, channelName):
        queue = exchanger.InternalQueue()
        self.queues.append(queue)
        self.hashes[channelName] = len(self.queues) - 1

        if channelType == "PUBLISH":
            threadDemo = exchanger.Publisher(self.host,
                                             self.port,
                                             self.username,
                                             self.password,
                                             channelName,
                                             queue)
            threadDemo.start()
            self.threads.append(threadDemo)
        if channelType == "SUBSCRIBE":
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

    def getQueue(self, name):
        return self.queues[self.hashes[name]]
