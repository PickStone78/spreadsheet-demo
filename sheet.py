# -*- coding:utf-8 -*-

from Tkinter import *
import ttk
import json

class SheetFrame:
    def __init__(self, parent, pool):
        self.frame = ttk.Frame(parent)
        self.pool = pool

        columnLabels = [ttk.Label(self.frame, text="{0}".format(x))
                        for x in range(5)]
        for i in range(5):
            columnLabels[i].grid(column=i+1, row=0, sticky=W)

        rowLabels = [ttk.Label(self.frame, text="{0}".format(x))
                     for x in range(9)]
        for i in range(9):
            rowLabels[i].grid(column=0, row=i+1, sticky=W)

        self.strVars = [StringVar() for x in range(5*9)]

        entryVars = [ttk.Entry(self.frame, textvariable=self.strVars[x])
                     for x in range(5*9)]
        for i in range(9):
            for j in range(5):
                entryVars[i*5+j].grid(column=j+1, row=i+1, sticky=W)

        initButton = ttk.Button(self.frame, text="初始化", command=self.initialize)
        initButton.grid(column=2, row=10, sticky=W)
        sendButton = ttk.Button(self.frame, text="发送", command=self.send)
        sendButton.grid(column=4, row=10, sticky=W)

    def initialize(self):
        streaming = []
        for i in range(5*9):
            x = self.strVars[i].get()
            if x:
                streaming.append({"ID":i, "FORMULA":x})

        self.pool.queues[0].push(json.dumps(streaming))

    def send(self):
        pass

    def update(self, flag):
        pass
