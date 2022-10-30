# -*- coding:utf-8 -*-
# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import requests
import base64
from playsound import playsound
import Play_mp3
import os
from LiMinTTS import tts_util
from weather_info import weather_info

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print ('start')
    weather_info = weather_info()
    weather_text = weather_info.text_info()
    print (weather_text)

    tts = tts_util()
    tts.speech(weather_text)

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
