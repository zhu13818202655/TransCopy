#!/usr/bin/python
# -*- coding: UTF-8 -*-
import tkinter as tk
from tkinter import scrolledtext
import readCopy
import testGoogletrans
old_text = ''
new_text = 'hi'
engine = readCopy.speakInit()
def update_timeText():
    global old_text
    global new_text
    new_text = readCopy.getCopyText()
    if new_text != old_text:
        scr.delete(0.0, tk.END)#清空之前的内容
        try:
            words = new_text
            result = testGoogletrans.translate(words)
            scr.insert(tk.END, result)
            old_text = new_text
            window.after(1000, update_timeText)
            return read_text(result)
        except:
            window.after(1000, update_timeText)
    else:
        window.after(1000, update_timeText)

def read_text(result):#读取
    global engine
    engine.say(result)
    engine.runAndWait()
def init():#对界面初始化
    window = tk.Tk()
    window.title('翻译机')
    window.geometry('600x300')
    Button1=tk.Button(window, text='再次朗读', command=lambda: read_text(result))
    Button1.pack(side='bottom')
    #Button1.place(anchor = 'se')
    Label1=tk.Label(window, text='结果:')
    Label1.place(x=10, y=10)
    # 滚动文本框
    scrolW = 30  # 设置文本框的长度
    scrolH = 10  # 设置文本框的高度
    scr = scrolledtext.ScrolledText(window, width=scrolW, height=scrolH, font=("隶书",14), wrap=tk.WORD)  # wrap=tk.WORD   这个值表示在行的末尾如果有一个单词跨行，会将该单词放到下一行显示, wrap默认的值为tk.CHAR
    scr.pack(side=tk.TOP, fill=tk.Y)  # side是滚动条放置的位置，上下左右。fill是将滚动条沿着y轴填充
    # columnspan 个人理解是将3列合并成一列   也可以通过 sticky=tk.W  来控制该文本框的对齐方式
    # 打包一个文本域到窗口，y方向滚动文本的监听丢给滚动条的set函数（文本域主动关联滚动条）
    return scr, window

if __name__ == "__main__":
    scr, window = init()
    engine = readCopy.speakInit()
    new_text = readCopy.getCopyText()
    try:
        words = new_text
        result = testGoogletrans.translate(words)
        # 拉动滚动条时，改变文本域在y方向上的视图（滚动条主动关联文本域）
        scr.insert(tk.END, result)
        update_timeText()
        window.wm_attributes('-topmost', 1)
        window.mainloop()
    except:
        pass


