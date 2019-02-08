#how to change speak speed
#参考：https://www.jianshu.com/p/0b4c9e9931f5C
import pyttsx3
engine = pyttsx3.init()
str = '茕茕孑立，沆瀣一气，踽踽独行，醍醐灌顶\
绵绵瓜瓞，奉为圭臬，龙行龘龘，犄角旮旯\
娉婷袅娜，涕泗滂沱\
呶呶不休，不稂不莠，卬咄嗟蹀躞耄耋饕餮\
囹圄蘡薁觊觎龃龉\
狖轭鼯轩，怙恶不悛\
其靁虺虺，腌臢孑孓\
陟罚臧否，针砭时弊，鳞次栉 比，一张一翕'
engine.say(str)
engine.say('hello world')
engine.say('你好，郭璞')
engine.runAndWait()
rate = engine.getProperty('rate') #获取当前引擎实例的属性值
volume = engine.getProperty('volume')

engine.setProperty('rate', rate-150)   #change speak speed减150
engine.setProperty('volume', volume-0.25)#change speak volume
voices = engine.getProperty('voices')
for voice in voices:
   print(voice .id)
   engine.setProperty('voice', voice.id)

   engine.say('The quick brown fox jumped over the lazy dog.')
   engine.say('要使用到剪贴板的方法，搜索到有两个包可以用')
engine.runAndWait()






'''
#借助微软的语音接口--"SAPI.SpVoice",对中文支持的不够好还有就是语速不能很好的控制
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
str1 = """
日照香炉生紫烟，
遥看瀑布挂前川。
飞流直下三千尺，
疑是银河落九天。
"""
speaker.Speak(str1)
for i in range(1, 6):
    speaker.Speak("呵呵第" + str(i) + "次")
speaker.Speak("Hello, it works!")
'''
