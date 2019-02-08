#参考：https://blog.csdn.net/nunchakushuang/article/details/75294947
import requests

def translate(content):

    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    data = {}
    data['i'] = content
    data['doctype'] = 'json'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    result = requests.post(url, data, headers=headers)
    print(result.text
          )
    trans = result.json()
    tran = trans['translateResult'][0][0]['tgt']

    return tran
if __name__ == '__main__':
    result = translate('I am a student')
    print(result)

