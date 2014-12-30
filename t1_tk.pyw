# -*- coding: gbk -*-
import re
from Tkinter import *

master = Tk()
wx = Canvas(master, width=600, height=400)
wx.pack()


t1_text= open('binary\\journal.txt','r')
t1_readlines=t1_text.readlines()

##t2_text = clientTCP.return_result()

son_tuple=[]
for line in t1_readlines:
    result=re.compile('浏览了(.*)次')
    answer=result.findall(line)
    try:
        son_tuple.append([line[:line.index('浏览了')],answer[0]])
    except:
        continue
sort_list=sorted(son_tuple,key=lambda x:x[1],reverse=True)
sored=1

#前五名称
desk_value=''

#高度列表
high_list=[]
for (i,j) in sort_list[:5]:
    desk_value+=str(sored)+'、'+i+'浏览了'+j+'次'+'\n'
    high_list.append(eval(j))
    sored+=1
##print high_list
##print desk_value
def count_high(x):
    return 370-(20*x)

#柱形名
wx.create_text(75,380,text ='1',fill='blue')
#柱形高度
wx.create_rectangle(65,370,90,count_high(high_list[0]), fill="red")

wx.create_text(105,380,text ='2',fill='blue')
wx.create_rectangle(95,370,120 ,count_high(high_list[1]), fill="blue")

wx.create_text(135,380,text ='3',fill='blue')
wx.create_rectangle(125,370,150,count_high(high_list[2]), fill="green")

wx.create_text(165,380,text ='4',fill='blue')
wx.create_rectangle(155,370,180,count_high(high_list[3]), fill="yellow")

wx.create_text(195,380,text ='5',fill='blue')
wx.create_rectangle(185,370,210,count_high(high_list[4]), fill="purple")

#直角坐标系
wx.create_line(60, 150, 60, 370,arrow='first',fill="gray")
wx.create_line(300, 370,60, 370,arrow='first',fill="gray")

#文字
wx.create_text(350,60,text = desk_value.decode('gbk'),fill='blue')

mainloop()

##print t2_text
