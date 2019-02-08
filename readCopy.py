#-*- coding: utf-8 -*-
import win32clipboard as wc#安装pywin32
import win32con
import pyttsx3
import chardet
import time

def speakInit():
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 120)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech_OneCore\Voices\Tokens\MSTTS_V110_zhCN_HongyuM")#HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0:这是英文的语音，只能阅读英文.\
    # 故用HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech_OneCore\Voices\Tokens\MSTTS_V110_zhCN_HongyuM替换HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0
    return  engine

def getCopyText():
    wc.OpenClipboard()
    try:
        copy_text= wc.GetClipboardData(win32con.CF_UNICODETEXT).replace("\r\n", " ").replace("\n", " ").replace("\r", " ")#win32con.CF_TEXT改成win32con.CF_UNICODETEXT
    except:
        copy_text = "no word"
    wc.CloseClipboard()

    return  copy_text


if __name__ == "__main__":
    old_text = "hi"
    engine = speakInit()
    while 1:

        time.sleep(1)
        #print(chardet.detect(getCopyText()))
        if getCopyText() != old_text:

            try:
                engine.say(getCopyText())
                time.sleep(1)
                engine.say(getCopyText())
                engine.runAndWait()
                old_text = getCopyText()
            except:
                pass
