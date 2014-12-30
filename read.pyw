# -*- coding: gbk -*-
import os
import re
print('数据扫描中....')
os.popen('read.bat')
print('数据写入中....')
buffer_files="binary\\journal.txt"
text = open(buffer_files,'a')
#text.writelines("你的ID是123456\n")
text.writelines("缓存文件:\n")
#获取文件夹里所有文件名
files_list = os.listdir( "binary\\buffer")
#为统计个数而设定
title_list=[]
#得到单个文件名
for files_name in files_list:
    try:
        files=open("binary\\buffer\\%s"%files_name).read().decode('utf-8') #转为unicode
        if '<title>' in files:
            result=re.compile('<title>(.*)</title>')
            answer=result.findall(files)
            #answer是列表
            for bit in answer:
##                print bit
##                text.writelines(str(files_name))
                #text.writelines(bit.encode('gbk'))#转为gbk
                #print bit
                #print files_name
                title_list.append(bit.encode('gbk'))
    #读取ansi的htm
    except (UnicodeDecodeError):
        files=open("binary\\buffer\\%s"%files_name).read()
        if '<title>' in files:
            result=re.compile('<title>(.*)</title>')
            answer=result.findall(files)
            for bit in answer:
##                print files_name
##                print bit
                #text.writelines(bit)
                title_list.append(bit)
#用字典统计次数
diction={}
for title in title_list:
    if title not in diction:
        diction[str(title)]=1
    else:
        diction[title]+=1
#py2.7写入字典是乱码,必须转化
for i in range(len(diction)):
    if len(str(diction.keys()[i]))>1:
        text.writelines(str(diction.keys()[i])+' 浏览了'+str(diction.values()[i])+'次\n')
print('完成！！')
text.close()
