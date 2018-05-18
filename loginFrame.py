#-*- coding: UTF-8 -*-
import wx

class LoginFrame(wx.Frame):
    def __init__(self, parent=None, id=-1, UpdateUI=None):
        wx.Frame.__init__(self, parent, id, title='登录系统', size=(600, 400))
        self.Centre()
        #self.themeColor='#0a74f7'
        self.BackgroundColour="white"
        self.UpdateUI = UpdateUI
        self.InitUI() # 绘制UI界面
    def OnEraseBack(self, event):
        dc = event.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        image = wx.Image('login.jpg', wx.BITMAP_TYPE_JPEG)
        image.Rescale(600, 400)
        bmp = image.ConvertToBitmap()
        dc.DrawBitmap(bmp, 0, 0)

    def InitUI(self):
        panel = wx.Panel(self)
        panel.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBack)
        font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, True)

        #accountLabel = wx.StaticText(panel, -1, '账 号', pos=(20, 30))
        accountLabel = wx.StaticText(panel, -1, '账 号', pos=(200, 150))
        #accountLabel.SetForegroundColour("#666666")
        accountLabel.SetFont(font)
        #TPStaticText(accountLabel)

        self.accountInput = wx.TextCtrl(panel, -1, u'', pos=(260, 145), size=(180, -1))
        self.accountInput.SetForegroundColour('gray')
        self.accountInput.SetFont(font)

        passwordLabel = wx.StaticText(panel, -1, '密 码', pos=(200, 195))
        passwordLabel.SetFont(font)
        #TPStaticText(passwordLabel)
        #passwordLabel.SetForegroundColour("#666666")

        self.passwordInput = wx.TextCtrl(panel, -1, u'', pos=(260, 190), size=(180, -1), style=wx.TE_PASSWORD)
        self.passwordInput.SetForegroundColour("#666666")
        self.passwordInput.SetFont(font)

        sureButton = wx.Button(panel, -1, u'登录', pos=(200, 250), size=(120, 40))
        sureButton.SetForegroundColour('white')
        sureButton.SetBackgroundColour("#666666")
        # 为【确定Button】绑定事件
        self.Bind(wx.EVT_BUTTON, self.sureEvent, sureButton)

        cancleButton = wx.Button(panel, -1, u'取消', pos=(340, 250), size=(120, 40))
        cancleButton.SetBackgroundColour('black')
        cancleButton.SetForegroundColour('#ffffff')
        # 为【取消Button】绑定事件
        self.Bind(wx.EVT_BUTTON, self.cancleEvent, cancleButton)

    def sureEvent(self, event):
        account = self.accountInput.GetValue()
        password = self.passwordInput.GetValue()
        # 通过回调函数传递数值
        if account=="cyh" and password=="123456":
            self.UpdateUI(2)
            self.Destroy()  # 销毁隐藏Dialog
        else:
            dlg = wx.MessageDialog(None, u"用户名或密码错误", u"信息提示", wx.YES_DEFAULT)
            if dlg.ShowModal() == wx.ID_YES:
                dlg.Destroy()

    def cancleEvent(self, event):
        self.Destroy()  # 销毁隐藏Dialog

