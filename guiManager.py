#-*- coding: UTF-8 -*-
import loginFrame
import From2
import From3
import From4
import From5
class GuiManager():
    def __init__(self, UpdateUI):
        self.UpdateUI = UpdateUI
        self.frameDict = {} # 用来装载已经创建的Frame对象

    def GetFrame(self, type):
        frame = self.frameDict.get(type)

        if frame is None:
            frame = self.CreateFrame(type)
            self.frameDict[type] = frame

        return frame

    def CreateFrame(self, type):
        if type == 0:
            return loginFrame.LoginFrame(parent=None, id=type, UpdateUI=self.UpdateUI)
        elif type == 2:
            return From2.From2(parent=None, id=type, UpdateUI=self.UpdateUI)
        elif type == 3:
            return From3.From3(parent=None, id=type, UpdateUI=self.UpdateUI)
        elif type == 4:
            return From4.From4(parent=None, id=type, UpdateUI=self.UpdateUI)
        elif type == 5:
            return From5.From5(parent=None, id=type, UpdateUI=self.UpdateUI)
