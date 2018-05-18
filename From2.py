#-*- coding: UTF-8 -*-
import wx
import sys
class From2(wx.Frame):
    C = 1.0
    kernel = "rbf"
    degree = 2
    gamma = 1
    coef0 = 0.0
    probability = False
    shrinking = True
    tol = 0.001
    cache_size = 200
    max_iter = -1
    def __init__(self, parent=None, id=-1, UpdateUI=None):
        wx.Frame.__init__(self, parent, id, title='安全态势评估系统', size=(850, 550))
        self.Centre()
        self.themeColor='#333333'
        self.UpdateUI = UpdateUI
        self.InitUI() # 绘制UI界面
        self.Bind(wx.EVT_CLOSE, self.OnExit)
    def OnEraseBack(self, event):
        dc = event.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        image = wx.Image('background.jpg', wx.BITMAP_TYPE_JPEG)
        image.Rescale(850,550)
        bmp = image.ConvertToBitmap()
        dc.DrawBitmap(bmp, 0, 0)
    def OnExit(self, event):
        sys.exit()
    def InitUI(self):
        panel = wx.Panel(self)
        panel.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBack)

        font = wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL, True)
        oneButton = wx.Button(panel, -1, u'配置参数', pos=(120, 145), size=(200, 60))
        oneButton.SetBackgroundColour('white')
        oneButton.SetForegroundColour(self.themeColor)
        oneButton.SetFont(font)
        # 为【确定Button】绑定事件
        self.Bind(wx.EVT_BUTTON, self.oneEvent, oneButton)

        twoButton = wx.Button(panel, -1, u'训练模块', pos=(120, 245), size=(200, 60))
        twoButton.SetBackgroundColour('white')
        twoButton.SetForegroundColour(self.themeColor)
        twoButton.SetFont(font)
        # 为【取消Button】绑定事件
        self.Bind(wx.EVT_BUTTON, self.twoEvent, twoButton)

        thereButton = wx.Button(panel, -1, u'测试模块', pos=(120, 350), size=(200, 60))
        thereButton.SetBackgroundColour('white')
        thereButton.SetForegroundColour(self.themeColor)
        thereButton.SetFont(font)
        # 为【取消Button】绑定事件
        self.Bind(wx.EVT_BUTTON, self.thereEvent, thereButton)

        fourButton = wx.Button(panel, -1, u'帮助', pos=(700, 450), size=(100, 30))
        fourButton.SetBackgroundColour('white')
        fourButton.SetForegroundColour(self.themeColor)
        fourButton.SetFont(font)
        self.Bind(wx.EVT_BUTTON, self.fourEvent, fourButton)
    def oneEvent(self, event):
        self.UpdateUI(3)

    def twoEvent(self, event):
        self.UpdateUI(4)
    def thereEvent(self, event):
        self.UpdateUI(5)
    def fourEvent(self, event):
        dlg = wx.MessageDialog(None, u"具体操作方法请参考《基于SVM的安全态势评估系统操作手册》!", u"信息提示", wx.YES_DEFAULT)
        if dlg.ShowModal() == wx.ID_YES:
            dlg.Destroy()


