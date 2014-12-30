# -*- coding: gbk -*-
import clientTCP
import re
from Tkinter import *

master = Tk()
wx = Canvas(master, width=600, height=400)
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
for (i,j) in sort_list[:5]:
    desk_value+=str(sored)+'、'.decode('gbk')+i+j+'\n'
    high_list.append(eval(j))
    sored+=1
####print high_list
####print desk_value
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
wx.create_text(350,60,text = desk_value,fill='blue')

mainloop()

####print t2_text
