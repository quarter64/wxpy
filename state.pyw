##encoding=utf-8
#!/usr/bin/env python
'''hello ,wxpython!program.'''
import wx
class Frame(wx.Frame):
    def __init__(self,image,parent=None,id=-1,pos=wx.DefaultPosition,
        title='免责声明!'.decode('utf-8')):
        temp=image.ConvertToBitmap()
        size = temp.GetWidth(), temp.GetHeight()
        wx.Frame.__init__(self, parent, id, title, pos, size)
        self.bmp = wx.StaticBitmap(parent=self, bitmap=temp)
class App(wx.App):
    def OnInit(self):
        image = wx.Image('two.jpg', wx.BITMAP_TYPE_JPEG)
        self.frame = Frame(image)
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True
app=App()
app.MainLoop()
##if __name__ == '__main__':
##    app=App()
##    app.MainLoop()
