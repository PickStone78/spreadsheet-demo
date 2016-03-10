# -*- coding:utf-8 -*-

from Tkinter import *
import ttk

class ConnectionFrame:
    def __init__(self, parent, pool):
        self.frame = ttk.Frame(parent)
        self.pool = pool

        hostLabel = ttk.Label(self.frame, text="主机")
        hostLabel.grid(column=0, row=0, sticky=W)
        portLabel = ttk.Label(self.frame, text="端口")
        portLabel.grid(column=2, row=0, sticky=W)

        self.host = StringVar()
        self.port = StringVar()
        hostEntry = ttk.Entry(self.frame, textvariable=self.host)
        hostEntry.grid(column=1, row=0, sticky=W)
        portEntry = ttk.Entry(self.frame, textvariable=self.port)
        portEntry.grid(column=3, row=0, sticky=W)

        usernameLabel = ttk.Label(self.frame, text="帐号")
        usernameLabel.grid(column=0, row=1, sticky=W)
        passwordLabel = ttk.Label(self.frame, text="密码")
        passwordLabel.grid(column=2, row=1, sticky=W)

        self.username = StringVar()
        self.password = StringVar()
        usernameEntry = ttk.Entry(self.frame, textvariable=self.username)
        usernameEntry.grid(column=1, row=1, sticky=W)
        passwordEntry = ttk.Entry(self.frame, textvariable=self.password)
        passwordEntry.grid(column=3, row=1, sticky=W)

        connectButton = ttk.Button(self.frame, text="连接", command=self.connect)
        connectButton.grid(column=4, row=1, sticky=W)
        closeButton = ttk.Button(self.frame, text="关闭", command=self.close)
        closeButton.grid(column=5, row=1, sticky=W)

        for child in self.frame.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def connect(self):
        self.pool.host = self.host.get()
        self.pool.port = int(self.port.get())
        self.pool.username = self.username.get()
        self.pool.password = self.password.get()
        self.pool.new("publish", "INITIALIZE")
        self.pool.new("subscribe", "STREAMING")

    def close(self):
        self.pool.clear()
