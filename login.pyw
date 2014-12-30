#encoding=gbk
import wx
import hashlib
from socket import * 

class AP_App(wx.App):
  def OnInit(self):
    frame = AP_MainFrame ("数据采集--交友平台", (420, 240), (400, 300))
    frame.Show()
    self.SetTopWindow(frame)
    
    loginPanel = AP_LoginPanel(frame)
    
    
    self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
    return True

  def OnCloseWindow (self, event):
##    self.Destroy()
    self.Close()



class AP_MainFrame(wx.Frame):
  def __init__(self, title, pos, size):    
    wx.Frame.__init__(self, None, -1, title, pos, size)
    self.CreateStatusBar()

class AP_LoginPanel(wx.Panel):
  def __init__(self, frame):

    
    
    self.frame = frame
    self.frame.SetStatusText("登陆认证!")

    
##    wx.Panel.__init__(self,frame)
##    image_file = 'two2.jpg'
##    bmp1 = wx.Image(image_file,wx.BITMAP_TYPE_ANY).ConvertToBitmap()
##    self.bitmap1 = wx.StaticBitmap(self,-1,bmp1,(0,0))

    
    self.panel = wx.Panel(frame)
    self.showLoginBox()
    self.panel.SetBackgroundColour('#009ACD')#009ACD' #1E90FF


  def showLoginBox (self):
    
  # Create the sizer
  #hgap和下个控件间距
    sizer = wx.FlexGridSizer(rows=3, cols=0, hgap=-160, vgap=15)

  # Username
    self.txt_Username = wx.TextCtrl(self.panel, 1, size=(150, -1))
    lbl_Username = wx.StaticText(self.panel,-1, "用户名:")
    #设置颜色
    lbl_Username.SetForegroundColour('#FFFFFF')
    sizer.Add(lbl_Username,0, wx.LEFT|wx.TOP| wx.RIGHT, 50)
    sizer.Add(self.txt_Username,0, wx.TOP| wx.RIGHT, 50)

  # Password
    self.txt_Password = wx.TextCtrl(self.panel, 1, size=(150, -1), style=wx.TE_PASSWORD)
    lbl_Password = wx.StaticText(self.panel, -1, "密码:")
    #设置颜色
    lbl_Password.SetForegroundColour('#FFFFFF')
    sizer.Add(lbl_Password,0, wx.LEFT|wx.RIGHT, 50)
    sizer.Add(self.txt_Password,0, wx.RIGHT, 50)

  # Submit button
    
    #按钮图片
    bmp = wx.Image("login.bmp", wx.BITMAP_TYPE_BMP).ConvertToBitmap()

##    btn_Process = wx.Button(self.panel, -1, "验证".decode('utf-8')) 
    self.button = wx.BitmapButton(self.panel, -1, bmp, pos=(10, 20))
    
    
    self.panel.Bind(wx.EVT_BUTTON, self.OnSubmit,self.button)# btn_Process)
    sizer.Add(self.button,0, wx.LEFT, 60)#(btn_Process,0, wx.LEFT, 80)

    self.panel.SetSizer(sizer)

  def OnSubmit(self, event):
    UserText = self.txt_Username.GetValue()
    PasswordText = self.txt_Password.GetValue()

    #被加密对象
    hash_by=str(PasswordText)
    hash_object=hashlib.md5()
    hash_object.update(hash_by)
    #被传送字符串
    convey='binary_timed_username_password'+str(UserText)+(hash_object.hexdigest())

    #发送数据至服务器
    host = 'localhost' 
    port = 3130 
    bufsize = 9999999 
    addr = (host,port) 
    client = socket(AF_INET,SOCK_STREAM) 
    client.connect(addr) 
    data = convey
    client.send('%s\r\n' % data)
    result = client.recv(bufsize)
    if result=='ok':
        buffer_files="binary\\journal.txt"
        text = open(buffer_files,'w')
        text.writelines("你的ID是%s\n"%str(UserText))
        text.close()

##        wx.EVT_QUERY_END_SESSION
        import clipboard
##        wx.GetApp().ExitMainLoop()
        wx.Exit()
      
    else:
        wx.MessageBox("用户名或密码错误\n请重新启动！","提示！")
        wx.Exit()
##        import setup

##        self.Close()
##        wx.Exit()
      

##    print convey
##    print UserText
##    print PasswordText

app = AP_App()  
app.MainLoop()
##if __name__ == '__main__':
##  app = AP_App()  
##  app.MainLoop()
