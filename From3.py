#-*- coding: UTF-8 -*-
import wx
from Data import *
class From3(wx.Frame):
    def __init__(self, parent=None, id=-1, UpdateUI=None):
        wx.Frame.__init__(self, parent, id, title='配置参数', size=(600, 370))
        self.Centre()
        self.themeColor='#333333'
        self.UpdateUI = UpdateUI
        self.InitUI() # 绘制UI界面
        self.Bind(wx.EVT_CLOSE, self.OnExit)
    def OnExit(self, event):
            self.UpdateUI(2)
    def InitUI(self):
        win = wx.Panel(self)
        font = wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL, True)
        #self.xxtext = wx.TextCtrl(win, wx.ID_ANY, pos=(110, 50), size=(350, 30))
        kernelList = ['linear', 'poly', 'rbf', 'sigmoid', 'precomputed']
        judgeList = ['是', '否']

        text1 = wx.StaticText(win, pos=(10, 25), label='请选择核函数:')
        self.kernelComboBox = wx.ComboBox(win, -1, value = "rbf", pos=(150, 20),size=(100, 20), choices = kernelList, style = wx.CB_DROPDOWN)

        text4 = wx.StaticText(win, pos=(300, 25), label='请输入惩罚系数C:')
        self.Ctext = wx.TextCtrl(win, wx.ID_ANY, value="1.0", pos=(440, 20), size=(100, 20))

        text5 = wx.StaticText(win, pos=(10, 55), label='poly函数的阶数n:')
        self.degreetext = wx.TextCtrl(win, wx.ID_ANY, value = "3",pos=(150, 50), size=(100, 20))

        text6 = wx.StaticText(win, pos=(300, 55), label='核函数的系数gamma:')
        self.gammatext = wx.TextCtrl(win, wx.ID_ANY, value = "-1",pos=(440, 50), size=(100, 20))

        text7 = wx.StaticText(win, pos=(10, 85), label='核函数的独立项c:')
        self.coef0text = wx.TextCtrl(win, wx.ID_ANY,value="0.0", pos=(150, 80), size=(100, 20))

        text8 = wx.StaticText(win, pos=(300, 85), label='启用概率估计:')
        self.probatext = wx.ComboBox(win, -1, value="否", pos=(440, 80), size=(100, 20), choices=judgeList,style=wx.CB_DROPDOWN)

        text9 = wx.StaticText(win, pos=(10, 115), label='启发式收缩方式:')
        self.shrinktext = wx.ComboBox(win, -1, value = "否", pos=(150, 110), size=(100, 20), choices = judgeList, style = wx.CB_DROPDOWN)

        text10 = wx.StaticText(win, pos=(300, 115), label='误差精度:')
        self.toltext = wx.TextCtrl(win, wx.ID_ANY,value="0.001", pos=(440, 110), size=(100, 20))

        text11 = wx.StaticText(win, pos=(10, 145), label='训练的内存:')
        self.cachesizetext = wx.TextCtrl(win, wx.ID_ANY,value="200", pos=(150, 140), size=(100, 20))

        text12 = wx.StaticText(win, pos=(300, 145), label='最大迭代次数:')
        self.maxitertest = wx.TextCtrl(win, wx.ID_ANY, value="-1",pos=(440, 140), size=(100, 20))

        oneButton = wx.Button(win, -1, u'确定', pos=(110, 250), size=(120, 40))
        oneButton.SetBackgroundColour('white')
        oneButton.SetForegroundColour(self.themeColor)
        # 为【确定Button】绑定事件
        self.Bind(wx.EVT_BUTTON, self.oneEvent, oneButton)

        twoButton = wx.Button(win, -1, u'取消', pos=(290, 250), size=(120, 40))
        twoButton.SetBackgroundColour('white')
        twoButton.SetForegroundColour(self.themeColor)
        # 为【取消Button】绑定事件
        self.Bind(wx.EVT_BUTTON, self.twoEvent, twoButton)

    def oneEvent(self, event):
        if self.kernelComboBox.GetValue() != "":
            self.kernel=self.kernelComboBox.GetValue()
            self.C = float(self.Ctext.GetValue())
            self.degree = int(self.degreetext.GetValue())
            self.gamma = float(self.gammatext.GetValue())
            if self.gamma == -1.0:
                self.gamma = "auto"
            self.coef0 = float(self.coef0text.GetValue())
            if self.probatext.GetValue() == "否":
                self.probability = False
            else:
                self.probability = True
            if self.shrinktext.GetValue() == "否":
                self.shrinking = False
            else:
                self.shrinking = True
            self.tol = float(self.toltext.GetValue())
            self.cache_size = float(self.cachesizetext.GetValue())
            self.max_iter = int(self.maxitertest.GetValue())
            #self.size = int(self.sizetext.GetValue())
            dlg = wx.MessageDialog(None, u"参数设定成功", u"信息提示", wx.YES_DEFAULT)
            if dlg.ShowModal() == wx.ID_YES:
                dlg.Destroy()
            #Data.size=self.size
            Data.kernel=self.kernel
            Data.C = self.C
            Data.degree = self.degree
            Data.gamma = self.gamma
            Data.coef0 = self.coef0
            Data.probability = self.probability
            Data.shrinking = self.shrinking
            Data.tol = self.tol
            Data.cache_size = self.cache_size
            Data.max_iter = self.max_iter
            self.UpdateUI(2)
        else:
            dlg = wx.MessageDialog(None, u"请输入正确的参数", u"信息提示", wx.YES_DEFAULT)
            if dlg.ShowModal() == wx.ID_YES:
                dlg.Destroy()


    def twoEvent(self, event):
        self.UpdateUI(2)