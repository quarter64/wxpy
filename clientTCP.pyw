# -*- coding: gbk -*- #
from socket import * 

def return_result():
    host = 'localhost' 
    port = 3130 
    bufsize = 99999999
    addr = (host,port) 
    client = socket(AF_INET,SOCK_STREAM) 
    client.connect(addr) 
    data = open('binary\\journal.txt').read()
    client.send('%s\r\n' % data) 
    result = client.recv(bufsize)
    client.close()
##    return result
    return_main_result=''
    for i in eval(result):
        for j in i:
            if len(j)==(6) or len(j)==(11):
                return_main_result+=j+'和你一起浏览了\n\n'.decode('gbk')
            else:
                return_main_result+=j
##    
##    for i in eval(result):
##        print i
    return return_main_result

#服务器返回数据排序
def t2_return_result():
    host = 'localhost' 
    port = 3130 
    bufsize = 99999999
    addr = (host,port) 
    client = socket(AF_INET,SOCK_STREAM) 
    client.connect(addr) 
    data = open('binary\\journal.txt').read()
    client.send('%s\r\n' % data) 
    result = client.recv(bufsize)
    client.close
    return result
if __name__=="__main__":
    a=return_result()
    print a
##print data
##client.send('%s\r\n' % data)
##data = client.recv(bufsize)

##while True: 
##    ##data = raw_input() 
##    if not data or data=='exit': 
##        break 
##    client.send('%s\r\n' % data) 
##    data = client.recv(bufsize) 
##    if not data: 
##        break 
##    print data#.strip() 

 
