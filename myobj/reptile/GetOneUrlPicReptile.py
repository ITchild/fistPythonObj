#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __Author__: 云海星空
import re
import tkinter
import tkinter.messagebox
import urllib.request
import os


# 定义获取网页源代码函数
def gethtml(url):
    papg = urllib.request.urlopen(url)  # 打开图片的网址
    html = papg.read()  # 用read方法读成网页源代码，格式为字节对象
    html = html.decode('GBK')  # 定义编码格式解码字符串(字节转换为字符串)
    return html

#
def action(baseUrl,path):
    html = gethtml(baseUrl)
    imgre = re.compile(r'href="(.*?)" title')  # 正则匹配，compile为把正则表达式编译成一个正则表达式对象，提供效率。
    imglist = re.findall(imgre, html)  # 获取字符串中所有匹配的字符串
    for secondUrl in imglist:
        secondHtml = gethtml(secondUrl)
        getimg(secondHtml,path)

# 匹配
def getimg(html, path):
    imgre = re.compile(r'"bdPic": "(.*?)"')  # 正则匹配，compile为把正则表达式编译成一个正则表达式对象，提供效率。
    imglist = re.findall(imgre, html)  # 获取字符串中所有匹配的字符串
    namere = re.compile(r'alt="(.*?)"')
    nameList = re.findall(namere, html)
    imgurl = imglist[0]
    for img in imglist:
        if img.endswith(".jpg"):
            imgurl = img
    if (not os.path.exists(path)):
        os.makedirs(path)
    urllib.request.urlretrieve("http://www.xiaohuar.com" + imgurl,
                                   path +'%s.jpg' % nameList[0])  # 把图片下载到本地并指定保存目录
    print("正在下载第%s张" % nameList[0])  # 格式化输出张数
    tkinter.messagebox.askokcancel("提示", "正在下载第%s张" % nameList[0])

# 调用函数
def getPic() :
    action('http://www.xiaohuar.com/html/sitemap.htm','D:\\pictures\\')


top = tkinter.Tk()
'''包名的行控件 START'''
pageFragme = tkinter.Frame(top)
lPage = tkinter.Label(pageFragme, text="检索网站")
lPage.pack(side="left")
pageName = tkinter.Entry(pageFragme)
pageName.insert(0, "中国校花网")
pageName.pack(side="right")
pageFragme.pack()
'''包名的行控件 END'''
'''运行次数的行控件 START'''
runNumFragme = tkinter.Frame(top)
runNumPage = tkinter.Label(runNumFragme, text="缓存目录")
runNumPage.pack(side="left")
runNum = tkinter.Entry(runNumFragme)
runNum.insert(0, "D盘的pictures文件夹下")
runNum.pack(side="right")
runNumFragme.pack()
'''运行次数的行控件 END'''

okButton = tkinter.Button(top, text="点击获取福利", command=getPic)
okButton.pack()
top.title("送福利")
ww = 200
wh = 150
x = top.winfo_screenwidth()
y = top.winfo_screenheight()
x = (x - ww) / 2
y = (y - wh) / 2
top.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
top.mainloop()

