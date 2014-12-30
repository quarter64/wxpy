# -*- coding: gbk -*-
import wx
import sys
import os
import read
import clientTCP
sys.stdout.close()
##wx.GetApp().ExitMainLoop()
t1_text = "我浏览过的\n"+open('binary\\journal.txt').read()
t2_text = '和我共同浏览的 \n'
t2_text = t2_text+clientTCP.return_result().encode('gbk')

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="数据采集———交友平台",
                          size=(900,600))

##        p1 = wx.Panel(self)
        menu = wx.Menu()
        bmp = wx.Bitmap("open.png", wx.BITMAP_TYPE_PNG)
        item = wx.MenuItem(menu, -1, "重新登录")
        item.SetBitmap(bmp)
        a=menu.AppendItem(item)
        self.Bind(wx.EVT_MENU, self.OnExi, a)

        bmp1 = wx.Bitmap("save.png", wx.BITMAP_TYPE_PNG)
        item1 = wx.MenuItem(menu, -1, "保存结果至本地")
        item1.SetBitmap(bmp1)
        save_local=menu.AppendItem(item1)
        self.Bind(wx.EVT_MENU, self.save_to_local,save_local)
        
        menu.AppendSeparator()
        bmp2 = wx.Bitmap("out.png", wx.BITMAP_TYPE_PNG)
        item2 = wx.MenuItem(menu, -1, "退出")
        item2.SetBitmap(bmp2)
        exit=menu.AppendItem(item2)
        self.Bind(wx.EVT_MENU, self.OnExit,exit)
                    
        menuBar = wx.MenuBar()
        menuBar.Append(menu, "菜单")


        menu2 = wx.Menu()
        
        bmp20 = wx.Bitmap("count.png", wx.BITMAP_TYPE_PNG)
        item20 = wx.MenuItem(menu2, -1, "本地数据统计")
        item20.SetBitmap(bmp20)
        title_count=menu2.AppendItem(item20)
        self.Bind(wx.EVT_MENU, self.count,title_count)

        bmp201 = wx.Bitmap("count1.png", wx.BITMAP_TYPE_PNG)
        item201 = wx.MenuItem(menu2, -1, "云数据统计")
        item201.SetBitmap(bmp201)
        title_count1=menu2.AppendItem(item201)
        self.Bind(wx.EVT_MENU, self.count1,title_count1)

        menu2.AppendSeparator()
        
        bmp21 = wx.Bitmap("del.png", wx.BITMAP_TYPE_PNG)
        item21 = wx.MenuItem(menu2, -1, "清除IE缓存")
        item21.SetBitmap(bmp21)
        del_buffer=menu2.AppendItem(item21)
        self.Bind(wx.EVT_MENU, self.del_buf,del_buffer)


        bmp211 = wx.Bitmap("del_local.png", wx.BITMAP_TYPE_PNG)
        item211 = wx.MenuItem(menu2, -1, "清除本地缓存")
        item211.SetBitmap(bmp211)
        del_local_buffer=menu2.AppendItem(item211)
        self.Bind(wx.EVT_MENU, self.del_local_buf,del_local_buffer)
        

        bmp22 = wx.Bitmap("static.png", wx.BITMAP_TYPE_PNG)
        item22 = wx.MenuItem(menu2, -1, "静态文本查看")
        item22.SetBitmap(bmp22)
        static_look=menu2.AppendItem(item22)
        self.Bind(wx.EVT_MENU, self.static,static_look)

        menuBar.Append(menu2, "选项")
        


        menu3 = wx.Menu()
        
        bmp31 = wx.Bitmap("title3.png", wx.BITMAP_TYPE_PNG)
        item31 = wx.MenuItem(menu3, -1, "免责声明")
        item31.SetBitmap(bmp31)
        title31=menu3.AppendItem(item31)
        self.Bind(wx.EVT_MENU, self.Event_title31,title31)
        
        menu3.AppendSeparator()

        bmp32 = wx.Bitmap("help.png", wx.BITMAP_TYPE_PNG)
        item32 = wx.MenuItem(menu3, -1, "帮助")
        item32.SetBitmap(bmp32)
        help_button=menu3.AppendItem(item32)
        self.Bind(wx.EVT_MENU, self.button,help_button)

        bmp33 = wx.Bitmap("about.png", wx.BITMAP_TYPE_PNG)
        item33 = wx.MenuItem(menu3, -1, "关于")
        item33.SetBitmap(bmp33)
        title_about=menu3.AppendItem(item33)
        self.Bind(wx.EVT_MENU, self.about,title_about)
        
        menuBar.Append(menu3, "开发者")

        
        self.SetMenuBar(menuBar)
  
        p = wx.Panel(self)


        p.SetBackgroundColour('#216856')

         
        # create the controls
        self.t1 = wx.TextCtrl(p, -1, t1_text,
                              style=wx.TE_MULTILINE|wx.HSCROLL)
        
        self.t1.SetForegroundColour('blue')


        self.t2 = wx.TextCtrl(p, -1, t2_text,
                              style=wx.TE_MULTILINE|wx.HSCROLL)
        self.t2.SetForegroundColour('#267612')
        
        
        copy = wx.Button(p, -1, "我的浏览量前5名柱状图")
        paste = wx.Button(p, -1, "和我一起浏览的柱状图")

        # setup the layout with sizers
        fgs = wx.FlexGridSizer(2, 2, 5, 5)
        fgs.AddGrowableRow(0)
        fgs.AddGrowableCol(0)
        fgs.AddGrowableCol(1)
        fgs.Add(self.t1, 0, wx.EXPAND)
        fgs.Add(self.t2, 0, wx.EXPAND)
        fgs.Add(copy, 0, wx.EXPAND)
        fgs.Add(paste, 0, wx.EXPAND)
        border = wx.BoxSizer()
        border.Add(fgs, 1, wx.EXPAND|wx.ALL, 5)
        p.SetSizer(border)

        # Bind events
        self.Bind(wx.EVT_BUTTON, self.OnDoCopy, copy)
        self.Bind(wx.EVT_BUTTON, self.OnDoPaste, paste)

    def OnDoCopy(self, evt):
        import t1_tk

    def OnDoPaste(self, evt):
        import t2_tk
            
    def OnExit(self, event):
        sys.exit(0)
        
    def OnExi(self,event):
        os.system('start.bat')
        sys.exit(0)
    def save_to_local(self,event):
        buffer_files="binary.txt"
        text = open(buffer_files,'w')
        text.write(t2_text)
        text.close()
        wx.MessageBox("数据已保存到binary.txt","提示！")
    def del_buf(self,event):
        os.system('del.bat')
        
    def static(self,event):
        import static
        
    def Event_title31(self,event):
        import state

    def button(self,event):
        wx.MessageBox("客户端版本号\nversion 1.0!","帮助！")

    def about(self,event):
        wx.MessageBox("适用于Microsoft Windows 7\n 以IE内核为浏览器的浏览数据","关于!")

    def count(self,event):
        import big_t1_tk

    def count1(self,event):
        import big_t2_tk
    def del_local_buf(self,event):
        os.system('del_local.bat')

app = wx.PySimpleApp()
frm = MyFrame()
frm.Show()
app.MainLoop()
