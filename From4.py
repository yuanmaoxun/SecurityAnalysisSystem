#-*- coding: UTF-8 -*-
import wx
import tkinter as tk
from tkinter import filedialog
from Data import *
import pandas as pd
import numpy as np
from sklearn.svm import SVC
class From4(wx.Frame):
    def __init__(self, parent=None, id=-1, UpdateUI=None):
        wx.Frame.__init__(self, parent, id, title='训练模型', size=(850, 550))
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
        image.Rescale(850, 550)
        bmp = image.ConvertToBitmap()
        dc.DrawBitmap(bmp, 0, 0)
    def InitUI(self):
        self.panel = wx.Panel(self)
        self.panel.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBack)
        font = wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL, True)
        oneButton = wx.Button(self.panel, -1, u'导入训练数据', pos=(60, 100), size=(200, 50))
        oneButton.SetForegroundColour(self.themeColor)
        oneButton.SetBackgroundColour('white')
        # 为【确定Button】绑定事件
        self.Bind(wx.EVT_BUTTON, self.oneEvent, oneButton)

        twoButton = wx.Button(self.panel, -1, u'开始训练', pos=(60, 200), size=(200, 50))
        twoButton.SetForegroundColour(self.themeColor)
        twoButton.SetBackgroundColour('white')
        # 为【确定Button】绑定事件
        self.Bind(wx.EVT_BUTTON, self.twoEvent, twoButton)

        thereButton = wx.Button(self.panel, -1, u'返回上一级', pos=(60, 300), size=(200, 50))
        thereButton.SetForegroundColour(self.themeColor)
        thereButton.SetBackgroundColour('white')
        # 为【确定Button】绑定事件
        self.Bind(wx.EVT_BUTTON, self.therEvent, thereButton)
        self.text = wx.TextCtrl(self.panel, wx.ID_ANY, pos=(300, 0), size=(640, 550), style=wx.TE_MULTILINE)
    def oneEvent(self, event):
        root = tk.Tk()
        root.withdraw()
        Data.x_fath = filedialog.askopenfilename()
        if(Data.x_fath!= ""):
            dlg = wx.MessageDialog(None, u"导入成功", u"信息提示", wx.YES_DEFAULT)
            if dlg.ShowModal() == wx.ID_YES:
                dlg.Destroy()
            self.text.Clear()
            self.text.write("打开文件：" + Data.x_fath + "\n")
            with open(Data.x_fath) as file:
                contents = file.read()
                self.text.write(contents)
    def twoEvent(self, event):
        print(Data.x_fath)
        df = pd.read_csv(Data.x_fath, encoding='utf-8')
        Data.colsize = np.array(df.ix[0,:]).size-1
        df.head()
        X = df.ix[:, :Data.colsize]
        Y = np.array(df.ix[:, Data.colsize]).astype(str)
        Data.clf = SVC(C=Data.C, kernel=Data.kernel, degree=Data.degree, gamma=Data.gamma, coef0=Data.coef0,
                       probability=Data.probability, shrinking=Data.shrinking, tol=Data.tol,
                       cache_size=Data.cache_size,class_weight=None,verbose=False, max_iter=Data.max_iter,random_state=None, decision_function_shape="ovo")
        Data.clf.fit(X, Y)
        dlg = wx.MessageDialog(None, u"分析完成！", u"信息提示", wx.YES_DEFAULT)
        if dlg.ShowModal() == wx.ID_YES:
            dlg.Destroy()
    def therEvent(self, event):
        self.UpdateUI(2)

