#-*- coding: UTF-8 -*-
import wx
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
from Data import *
import pandas as pd

# 解决图表中文乱码问题
plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文字体设置
plt.rcParams['axes.unicode_minus'] = False
class From5(wx.Frame):
    def __init__(self, parent=None, id=-1, UpdateUI=None):
        wx.Frame.__init__(self, parent, id, title='测试模型', size=(920, 550))
        self.Centre()
        self.themeColor='#333333'
        self.UpdateUI = UpdateUI
        self.InitUI() # 绘制UI界面
        self.Bind(wx.EVT_CLOSE, self.OnExit)
    def OnExit(self, event):
        self.UpdateUI(2)
    def OnEraseBack(self, event):
        dc = event.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        image = wx.Image('background.jpg', wx.BITMAP_TYPE_JPEG)
        image.Rescale(920, 550)
        bmp = image.ConvertToBitmap()
        dc.DrawBitmap(bmp, 0, 0)
    def InitUI(self):
        self.panel = wx.Panel(self)
        self.panel.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBack)
        font = wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
        oneButton = wx.Button(self.panel, -1, u'导入评估数据', pos=(60, 30), size=(200, 50))
        oneButton.SetForegroundColour(self.themeColor)
        oneButton.SetBackgroundColour('white')
        # 为【确定Button】绑定事件
        self.Bind(wx.EVT_BUTTON, self.oneEvent, oneButton)

        twoButton = wx.Button(self.panel, -1, u'输出评估结果', pos=(60, 130), size=(200, 50))
        twoButton.SetForegroundColour(self.themeColor)
        twoButton.SetBackgroundColour('white')
        # 为【确定Button】绑定事件
        self.Bind(wx.EVT_BUTTON, self.twoEvent, twoButton)

        thereButton = wx.Button(self.panel, -1, u'输入评估数据', pos=(60, 230), size=(200, 50))
        thereButton.SetForegroundColour(self.themeColor)
        thereButton.SetBackgroundColour('white')
        # 为【确定Button】绑定事件
        self.Bind(wx.EVT_BUTTON, self.thereEvent, thereButton)

        fourButton = wx.Button(self.panel, -1, u'输出评估结果', pos=(60, 330), size=(200, 50))
        fourButton.SetForegroundColour(self.themeColor)
        fourButton.SetBackgroundColour('white')
        # 为【确定Button】绑定事件
        self.Bind(wx.EVT_BUTTON, self.fourEvent, fourButton)

        fiveButton = wx.Button(self.panel, -1, u'返回上一级', pos=(60, 430), size=(200, 50))
        fiveButton.SetForegroundColour(self.themeColor)
        fiveButton.SetBackgroundColour('white')
        # 为【确定Button】绑定事件
        self.Bind(wx.EVT_BUTTON, self.fiveEvent, fiveButton)

    def oneEvent(self, event):
        root = tk.Tk()
        root.withdraw()
        Data.c_fath = filedialog.askopenfilename()
        if(Data.c_fath!= ""):
            dlg = wx.MessageDialog(None, u"导入成功", u"信息提示", wx.YES_DEFAULT)
            if dlg.ShowModal() == wx.ID_YES:
                dlg.Destroy()
    def twoEvent(self, event):

        df1 = pd.read_csv(Data.c_fath, encoding='utf-8')
        df1.head()
        X1 = df1.ix[:, :Data.colsize]
        y_pred = Data.clf.predict(X1)
        plt.figure()
        i=1
        for value in y_pred:
            if(value=="M"):
                plt.bar(i, 0.5,color='blue', width=0.4, alpha=0.3)
                #plt.hlines(0.5, 1, i, colors="blue", linestyles="dashed")
            elif(value=="H"):
                plt.bar(i, 0.8, color='green', width=0.4, alpha=0.3)
                #plt.hlines(0.8, 1, i, colors="red", linestyles="dashed")
            elif(value=="L"):
                plt.bar(i, 0.2, color='red', width=0.4, alpha=0.3)
                #plt.hlines(0.2, 1, i, colors="green", linestyles="dashed")
            i=i+1
        scale_ls = [0,0.2,0.5,0.8]
        index_ls = ['无','低', '中', '高']
        plt.yticks(scale_ls,index_ls)
        #plt.bar(x,y,width=0.4,alpha=0.3)
        plt.title("测试结果")
        plt.xlabel("组别")
        plt.ylabel("安全性水平")
        plt.savefig("groupplot.png")
        image = wx.Image('groupplot.png', wx.BITMAP_TYPE_PNG)
        temp = image.ConvertToBitmap()
        wx.StaticBitmap(parent=self.panel, bitmap=temp,pos=(300, 5))
    def thereEvent(self, event):
        app = MyCollectApp()
        app.mainloop()

    def fourEvent(self, event):
        y_pred = Data.clf.predict(Data.s_X)
        plt.figure()

        for value in y_pred:
            if (value == "M"):
                plt.bar(1, 0.5, color='blue', width=0.4, alpha=0.3)
                # plt.hlines(0.5, 1, i, colors="blue", linestyles="dashed")
            elif (value == "H"):
                plt.bar(1, 0.8, color='green', width=0.4, alpha=0.3)
                # plt.hlines(0.8, 1, i, colors="red", linestyles="dashed")
            elif (value == "L"):
                plt.bar(1, 0.2, color='red', width=0.4, alpha=0.3)
        scaley_ls = [0, 0.2, 0.5, 0.8]
        indey_ls = ['无','低', '中', '高']
        scalex_ls = [1]
        index_ls = ['1']
        plt.yticks(scaley_ls, indey_ls)
        plt.xticks(scalex_ls, index_ls)
        # plt.bar(x,y,width=0.4,alpha=0.3)
        plt.title("测试结果")
        plt.xlabel("组别")
        plt.ylabel("安全性水平")
        plt.savefig("oneplot.png")
        image = wx.Image('oneplot.png', wx.BITMAP_TYPE_PNG)
        temp = image.ConvertToBitmap()
        wx.StaticBitmap(parent=self.panel, bitmap=temp, pos=(300, 5))
    def fiveEvent(self, event):
        self.UpdateUI(2)

class MyCollectApp(tk.Toplevel):#重点
    def __init__(self):
        super().__init__() #重点
        self.title('请输入测试数据')
        self.setupUI()

    def setupUI(self):
        row1 = tk.Frame(self)
        row1.pack(ipadx=70,ipady= 20)

        l1 = tk.Label(row1, text="请输入数据，以逗号分隔数据",height=3,width=30)
        l1.pack(side=tk.TOP)  # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM

        self.xls_text = tk.StringVar()
        tk.Entry(row1, textvariable=self.xls_text).pack(ipadx=140,ipady=5,pady=8)

        tk.Button(row1, text="确定", command=self.on_click).pack(ipadx=40,ipady= 5, pady=40)


    def on_click(self):
        str1 = self.xls_text.get().lstrip()
        try:
            if str1.count(",") != Data.colsize - 1:
                dlg = wx.MessageDialog(None, u"输入测试数据格式不正确", u"信息提示", wx.YES_DEFAULT)
                if dlg.ShowModal() == wx.ID_YES:
                    dlg.Destroy()
            else:
                a = str1.split(",", str1.count(","))
                Data.s_X = np.vstack((a, a))
                dlg = wx.MessageDialog(None, u"输入完成", u"信息提示", wx.YES_DEFAULT)
                if dlg.ShowModal() == wx.ID_YES:
                    dlg.Destroy()
                self.quit()
                self.destroy()
        except:
            dlg = wx.MessageDialog(None, u"未输入维度", u"信息提示", wx.YES_DEFAULT)
            if dlg.ShowModal() == wx.ID_YES:
                dlg.Destroy()
