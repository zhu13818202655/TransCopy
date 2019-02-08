***copytransvoide.py将剪贴板的英文段落翻译并语音播报***

补充：
1.将googletrans库中文件中所有的translate.google.com换成translate.google.cn
2.运用了mtranslate库，但是由于国内防火墙的缘故，需要将mtranslate中的core.py文件中的 
base_link = "http://translate.google.com/m?hl=%s&sl=%s&q=%s"
改成 base_link = "http://translate.google.cn/m?hl=%s&sl=%s&q=%s"

## 关于控件的位置
.pack(side='position')#position:TOP  靠上对齐；BOTTOM  靠下对齐；LEFT 靠左对齐；RIGHT      靠右对齐
.place(anchor='position')#position:n,w,e,s,ne,nw,se,ss