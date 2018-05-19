#-*- coding: UTF-8 -*-
import wx
import guiManager as FrameManager

class MainAPP(wx.App):

    def OnInit(self):
        self.manager = FrameManager.GuiManager(self.UpdateUI)
        self.frame = self.manager.GetFrame(2)
        self.frame.Show()
        return True

    def UpdateUI(self, type):
        self.frame.Show(False)
        self.frame = self.manager.GetFrame(type)
        self.frame.Show(True)

def main():
    app = MainAPP()
    app.MainLoop()

if __name__ == "__main__":
    main()