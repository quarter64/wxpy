# -*- coding: utf-8 -*-
import wx

class StaticTextFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None, -1, '静态文本显示'.decode('utf-8'),
        size=(750, 500))
        panel = wx.Panel(self, -1)
        panel.SetBackgroundColour('#216856')
        # 这是一个基本的静态文本
        files=open("binary//journal.txt").read().decode('gbk')
        text=wx.StaticText(panel, -1,'你的数据:\n%s'.decode('utf-8')%files,
        (0, 0),style=wx.ALIGN_LEFT)
        text.SetForegroundColour('#999999')
app =wx.PySimpleApp(redirect=True)
frame = StaticTextFrame()
frame.Show(True)
app.MainLoop()
