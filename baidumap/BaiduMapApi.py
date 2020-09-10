import tkinter
import tkinter.messagebox
from tkinter import *
import requests
import json
import time

top = tkinter.Tk()
top.title("百度检索")


sw = top.winfo_screenwidth()
#得到屏幕宽度
sh = top.winfo_screenheight()
#得到屏幕高度
ww = 300
wh = 200
#窗口宽高为100
x = (sw-ww) / 2
y = (sh-wh) / 2
top.geometry("%dx%d+%d+%d" %(ww,wh,x,y))


### 创建关键字输入框
query = Label(top, text='关键字')
query.grid(row=1)

queryE = Entry(top, bd=2)
queryE.grid(row=1, column=1)

### 创建地区输入框
region = Label(top, text='地区')
region.grid(row=2)

regionE = Entry(top)
regionE.grid(row=2, column=1)

filePath = ""

def tips(message):
    tkinter.messagebox.showinfo('提示',message)

page_size = 20

def getData():
    print(queryE.get() + " , " + regionE.get())
    query = queryE.get()
    page_num = 0
    url1 = 'http://api.map.baidu.com/place/v2/search?query=%s&tag=&region=%s&output=json&page_size=%d&page_num=%d&ak=UhEnmttUKI1jxbjMfUnG5lpQqqTuKiat' % (query, regionE.get(), page_size, page_num)
    reps = requests.get(url1)
    d = json.loads(reps.text)
    if d["status"] == 301:
        # 配额超限
        tips()
    elif d["status"] == 0:
        total = d["total"]
        num = int((total + page_size - 1) / page_size)
        print(num)
        filePath = query + time.strftime("%Y-%m-%d_%H%M%S") + ".csv"
        f = open(filePath, mode="a")
        for i in range(0,num):
            page_num = i
            url = 'http://api.map.baidu.com/place/v2/search?query=%s&tag=&region=%s&output=json&page_size=%d&page_num=%d&ak=UhEnmttUKI1jxbjMfUnG5lpQqqTuKiat' % (
            query, regionE.get(), page_size, page_num)
            print(url)
            rep = requests.get(url)
            # print(json.text)
            data = json.loads(rep.text)
            results = data["results"]

            for result in results:
                name = result["name"]
                location = result["location"]
                lat = location["lat"]
                lng = location["lng"]
                f.write(name + "," + str(lat) + "," + str(lng) + "\n")
        if f.closed == False :
            f.close()
        tips("文件%s已导出" % (filePath))
    else:
        tips("查询失败")

# 创建提交按钮
b = Button(top, text="查询", command=getData, width=5,height=2)
b.grid(row=3, column=1, sticky=W, pady=5)

top.mainloop()