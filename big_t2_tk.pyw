# -*- coding: gbk -*-
import clientTCP
import re
from Tkinter import *

master = Tk()
wx = Canvas(master, width=700, height=500)
wx.pack()


##t1_text= open('D:\\binary\\journal.txt','r')
##t1_readlines=t1_text.readlines()

t2_text = clientTCP.t2_return_result()
son_tuple=[]
for i in eval(t2_text):
    for line in i:
##for line in t1_readlines:
        result=re.compile('浏览了(.*)次'.decode('gbk'))
        answer=result.findall(line)
        try:
            son_tuple.append([line[:line.index('浏览了'.decode('gbk'))],answer[0]])
        except:
            continue
sort_list=sorted(son_tuple,key=lambda x:x[1],reverse=True)
##print sort_list
sored=1

#前五名称
desk_value=''

#高度列表
high_list=[]
for (i,j) in sort_list[:10]:
    desk_value+=str(sored)+'、'.decode('gbk')+i+j+'\n'
    high_list.append(eval(j))
    sored+=1
####print high_list
####print desk_value
def count_high(x):
    return 480-(20*x)

#柱形名
wx.create_text(75,480,text ='1',fill='blue')
#柱形高度
wx.create_rectangle(65,470,90,count_high(high_list[0]), fill="red")

wx.create_text(105,480,text ='2',fill='blue')
wx.create_rectangle(95,470,120 ,count_high(high_list[1]), fill="blue")

wx.create_text(135,480,text ='3',fill='blue')
wx.create_rectangle(125,470,150,count_high(high_list[2]), fill="green")

wx.create_text(165,480,text ='4',fill='blue')
wx.create_rectangle(155,470,180,count_high(high_list[3]), fill="yellow")

wx.create_text(195,480,text ='5',fill='blue')
wx.create_rectangle(185,470,210,count_high(high_list[4]), fill="purple")

wx.create_text(225,480,text ='6',fill='blue')
wx.create_rectangle(215,470,240,count_high(high_list[5]), fill="orange")

wx.create_text(255,480,text ='7',fill='blue')
wx.create_rectangle(245,470,270,count_high(high_list[6]), fill="#5E6BA2")

wx.create_text(285,480,text ='8',fill='blue')
wx.create_rectangle(275,470,300,count_high(high_list[7]), fill="#627612")

wx.create_text(315,480,text ='9',fill='blue')
wx.create_rectangle(305,470,330,count_high(high_list[8]), fill="#0E7B0E")

wx.create_text(345,480,text ='10',fill='blue')
wx.create_rectangle(335,470,360,count_high(high_list[9]), fill="#079FC6")

#直角坐标系
wx.create_line(60, 250, 60, 470,arrow='first',fill="gray")
wx.create_line(400, 470,60, 470,arrow='first',fill="gray")

#文字
wx.create_text(350,115,text = desk_value,fill='blue')

mainloop()
