#! /usr/bin/python
# -*- coding:utf-8 -*-

from Tkinter import *
import ttk
import sheet
import connection
import pool

pool = pool.ThreadPool()

# 根节点
root = Tk()
root.title("计算表格")
root.option_add('*tearOff', FALSE)

# 菜单
menubar = Menu(root)
root['menu'] = menubar
menuFile = Menu(menubar)
menubar.add_cascade(menu=menuFile, label="文件")
menuHelp = Menu(menubar)
menubar.add_cascade(menu=menuHelp, label="帮助")

sheetFrame = sheet.SheetFrame(root, pool)
sheetFrame.frame.grid(column=0, row=1, sticky=(N, W, E, S))

#
connectionFrame = connection.ConnectionFrame(root, pool)
connectionFrame.frame.grid(column=0, row=0, sticky=(N, W, E, S))

#
root.mainloop()
