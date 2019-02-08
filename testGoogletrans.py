#-*- coding: utf-8 -*-

#将googletrans库中文件中所有的translate.google.com换成translate.google.cn
from googletrans import Translator

def translate(sendwords):
    translator = Translator()
    return (translator.translate(sendwords,dest='zh-CN').text)



if __name__ == "__main__":
    words= "We trained a large, deep convolutional neural network"
    print(translate(words))




