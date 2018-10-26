#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __Author__: 云海星空
import re
import tkinter.messagebox
import urllib.request
import os
import _thread
from tkinter import END

class cation(object) :
    stopFlag = False

# 定义获取网页源代码函数
def gethtml(url):
    papg = urllib.request.urlopen(url)  # 打开图片的网址
    html = papg.read()  # 用read方法读成网页源代码，格式为字节对象
    html = html.decode('GBK')  # 定义编码格式解码字符串(字节转换为字符串)
    return html

#
def action(baseUrl, path):
    html = gethtml(baseUrl)
    imgre = re.compile(r'href="(.*?)" title')  # 正则匹配，compile为把正则表达式编译成一个正则表达式对象，提供效率。
    imglist = re.findall(imgre, html)  # 获取字符串中所有匹配的字符串
    if not path.endswith('/') :
        path = path + "/"
    if (not os.path.exists(path)):
        try:
            os.makedirs(path)
            message.insert(END, "创建存储目录 \n")
        except :
            message.insert(END, "创建存储目录失败，请检查您的存储路径 \n")
            return
    for secondUrl in imglist:
        if(not cation.stopFlag) :
            message.insert(END, "正在获取%s \n" % secondUrl)
            secondHtml = gethtml(secondUrl)
            message.insert(END, "正在解析... \n")
            getimg(secondHtml, path)
        else:
            message.insert(END,"停止成功 \n")
            break


# 匹配
def getimg(html, path):
    imgre = re.compile(r'"bdPic": "(.*?)"')  # 正则匹配，compile为把正则表达式编译成一个正则表达式对象，提供效率。
    imglist = re.findall(imgre, html)  # 获取字符串中所有匹配的字符串
    namere = re.compile(r'alt="(.*?)"')
    nameList = re.findall(namere, html)
    message.insert(END, "获取到图片名称%s \n" % nameList[0])
    imgurl = imglist[0]
    for img in imglist:
        if img.endswith(".jpg"):
            imgurl = img
    imgurl = "http://www.xiaohuar.com" + imgurl
    message.insert(END, "获取到图片路径%s \n" % imgurl)
    urllib.request.urlretrieve(imgurl,path + '%s.jpg' % nameList[0])  # 把图片下载到本地并指定保存目录
    print("正在下载第%s张" % nameList[0])  # 格式化输出张数
    message.insert(END,"正在下载%s图片\n" % nameList[0])
    message.see(END)
    message.update()

# 调用函数
def getPic():
    # 开启一个子线程
    cation.stopFlag = False
    message.insert(END,"开启分析线程\n")
    path = runNum.get()+""
    _thread.start_new_thread(
        action('http://www.xiaohuar.com/html/sitemap.htm', path),
        ("Thread-1", 2,))
def stopGetPic() :
    cation.stopFlag = True

top = tkinter.Tk()
'''包名的行控件 START'''
pageFragme = tkinter.Frame(top)
lPage = tkinter.Label(pageFragme, text="检索网站：")
lPage.pack(side="left")
pageName = tkinter.Label(pageFragme,text="中国校花网")
pageName.pack(side="right")
pageFragme.pack()
'''包名的行控件 END'''
'''运行次数的行控件 START'''
runNumFragme = tkinter.Frame(top)
runNumPage = tkinter.Label(runNumFragme, text="缓存目录")
runNumPage.pack(side="left")
runNum = tkinter.Entry(runNumFragme)
runNum.insert(0, "D://picture/福利/")
runNum.pack(side="right")
runNumFragme.pack()
'''运行次数的行控件 END'''

btFragme = tkinter.Frame(top)
okButton = tkinter.Button(btFragme, text="点击获取福利", command=getPic)
okButton.pack(side="left")
cancelButton = tkinter.Button(btFragme, text="停止获取福利", command=stopGetPic)
cancelButton.pack(side="right")
btFragme.pack()

sorcllBar = tkinter.Scrollbar(top)
message = tkinter.Text(sorcllBar)
message.pack()
sorcllBar.pack()


top.title("送福利")
ww = 300
wh = 450
x = top.winfo_screenwidth()
y = top.winfo_screenheight()
x = (x - ww) / 2
y = (y - wh) / 2
top.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
top.mainloop()
