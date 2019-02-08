from tkinter import *
from tkinter import messagebox
import requests

# 创建窗口
root = Tk()
# 标题
root.title('中英互译')
# 窗口大小
root.geometry('370x100')
# 窗口位置
# root.geometry('+600+450')
s_with = root.winfo_screenwidth()  # 获取屏幕宽
s_height = root.winfo_screenheight()  # 获取屏幕高度
# 计算页面打开在屏幕中央的位置
l_x = str(round((s_with - 370) / 2))
l_y = str(round((s_height - 100) / 2))
root.geometry('+' + l_x + '+' + l_y)
# 第一列标签
lable = Label(root, text='请输入内容：')
# 定位布局 grid网格式布局 pack包 place位置
lable.grid()
# 输入控件
extry = Entry(root, font=('微软雅黑', 15))
extry.grid(row=0, column=1)
res = StringVar()
# 翻译结果标签
lable1 = Label(root, text='翻译结果：')
lable1.grid(row=1, column=0)
# 翻译结果输入框
extry1 = Entry(root, font=('微软雅黑', 15), textvariable=res)
extry1.grid(row=1, column=1)


# 翻译方法
def translate():
    content = extry.get()
    content = content.strip()
    if content == '':
        messagebox.showinfo('提示', '请输入翻译内容')
    else:
        url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
        data = {}
        data['i'] = content
        #data['from'] = 'AUTO'
        #data['to'] = 'AUTO'
        #data['smartresult'] = 'dict'
        #data['client'] = 'fanyideskweb'
        #data['salt'] = '1538295833420'
        #data['sign'] = '07'
        data['doctype'] = 'json'
        #data['version'] = '2.1'
        #data['keyfrom'] = 'fanyi.web'
        #data['action'] = 'FY_BY_REALTIME'
        #data['typoResult'] = 'false'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
        result = requests.post(url, data, headers=headers)
        trans = result.json()
        print(trans)
        tran = trans['translateResult'][0][0]['tgt']
        res.set(tran)


# 按钮
button = Button(root, text='翻译', width='10', command=translate)
# sticky 对齐方式 N S W E 上下左右
button.grid(row=2, column=0, sticky=W)

# 退出按钮 command是点击事件的方法
exit_button = Button(root, text='退出', width='10', command=root.quit)
exit_button.grid(row=2, column=1, sticky=E)

# 显示窗口 消息循环 接收对窗口的所有操作的消息
root.mainloop()
