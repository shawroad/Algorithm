"""

@file   : 语音合成.py

@author : xiaolu

@time   : 2019-09-23

"""
'''
使用方法:
    网址: https://console.bce.baidu.com/ai/?_=1569224386927&fromai=1#/ai/speech/app/list
'''
from aip import AipSpeech

# APP_ID = '17317200'
# API_KEY = '775RqMWjqMrCjCLdKXTFq8BH'
# SECRET_KEY = 's5RNqRe7cK7zigVV8yZ29tHmrhKcaoCV'


APP_ID = '17317634'
API_KEY = 'B8VknEdLqiB2XSO3B5AgfX67'
SECRET_KEY = '1Ya6cD9y35xlOLNkubXn02e93NW9M6dy'


text = input("请输入要转化的文本:")
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
result = client.synthesis(text=text, options={'vol': 5})

if not isinstance(result, dict):
    with open('my_audio.mp3', 'wb') as f:
        f.write(result)
else:
    print(result)
