# -*- coding: gbk -*-
import os
import re
print('����ɨ����....')
os.popen('read.bat')
print('����д����....')
buffer_files="binary\\journal.txt"
text = open(buffer_files,'a')
#text.writelines("���ID��123456\n")
text.writelines("�����ļ�:\n")
#��ȡ�ļ����������ļ���
files_list = os.listdir( "binary\\buffer")
#Ϊͳ�Ƹ������趨
title_list=[]
#�õ������ļ���
for files_name in files_list:
    try:
        files=open("binary\\buffer\\%s"%files_name).read().decode('utf-8') #תΪunicode
        if '<title>' in files:
            result=re.compile('<title>(.*)</title>')
            answer=result.findall(files)
            #answer���б�
            for bit in answer:
##                print bit
##                text.writelines(str(files_name))
                #text.writelines(bit.encode('gbk'))#תΪgbk
                #print bit
                #print files_name
                title_list.append(bit.encode('gbk'))
    #��ȡansi��htm
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
#���ֵ�ͳ�ƴ���
diction={}
for title in title_list:
    if title not in diction:
        diction[str(title)]=1
    else:
        diction[title]+=1
#py2.7д���ֵ�������,����ת��
for i in range(len(diction)):
    if len(str(diction.keys()[i]))>1:
        text.writelines(str(diction.keys()[i])+' �����'+str(diction.values()[i])+'��\n')
print('��ɣ���')
text.close()
