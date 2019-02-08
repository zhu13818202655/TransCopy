from mtranslate import translate
'''
运用了mtranslate库，但是由于国内防火墙的缘故，需要将mtranslate中的core.py文件中的 
base_link = "http://translate.google.com/m?hl=%s&sl=%s&q=%s"
改成 base_link = "http://translate.google.cn/m?hl=%s&sl=%s&q=%s"
'''

def main():
    to_translate = '世间的一切都有标价，除了时间，一秒就是一秒，谁都无法讨价还价。\
于是我总在出差，把生命中的每分每秒都贡献给工作，因为我坚信创造财富才是时间的正经归宿。45岁时，我成为一个有事业和资本的成功人士，但妻子和儿子离开了我。'
    print(translate(to_translate))
    print(translate(to_translate, 'en'))
    print(translate(to_translate, 'ja'))

if __name__ == '__main__':
    main()