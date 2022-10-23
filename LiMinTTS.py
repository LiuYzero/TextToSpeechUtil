# -*- coding:utf-8 -*-

##################################
# 基于在线tts接口的tts转换/播放类
# 基于http://www.liminba.com/tool_api/tts.php接口获取mp3文件，并播放
#    依赖
#    pip install requests playsound play_mp3
#    apt install sox libsox-fmt-all
# @Author: LiuYang
# @Date: 2022-10-23
#################################

import requests
import base64
from playsound import playsound
import Play_mp3
import os

class tts_util(object):
    """
    支持windows,linux,termux, 不支持wsl

    """

    url = "http://www.liminba.com/tool_api/tts.php"
    filename = "foo.mp3"

    def __init__(self):
        None

    def speech(self, text, filename="foo.mp3"):
        """
        tts播放文字音频
        :param text: 文字
        :param filename: 音频文件
        :return: 无
        """
        print ("on speed method inside, filename is "+filename)
        self.filename = filename
        is_conver_success = self.covert_text_to_mp3(text, filename)
        if(is_conver_success == 1):
            print ("text to mp3 faild")

        self.play(self.filename)

    def covert_text_to_mp3(self, text, filename):
        """
        转换文字到mp3文件
        :param text:  需要转换为音频的文字
        :param filename: 转换后mp3文件名称
        :return: 0 | 1
        """
        payload = {
            "type": "tn",
            "spd": 5,
            "pit": 5,
            "vol": 5,
            "dt": 5,
            "peer": 4115,
            "tex": text
        }
        headers = {}

        response = requests.request("POST", self.url, headers=headers, data=payload)
        # print (response.text)

        audio_content_base64 = self.filter_response(response)
        # print (audio_content_base64)
        if(audio_content_base64 == ""):
            return 1

        self.write_mp3_by_base64_content(audio_content_base64, filename)

        return 0


    def filter_response(self, response):
        default_format = "data:audio/x-mpeg;base64,"
        if response.text.find(default_format) != -1:
            print("is audio in base64")
            return response.text.replace(default_format, "")
        else:
            print("not audio in base64")
            return ""

    def write_mp3_by_base64_content(self, audio_content_base64, filename="foo.mp3"):
        with open(filename, "wb") as temp_file:
            temp_file.write(base64.b64decode(audio_content_base64))
        print (filename + "writed")


    def play_with_sox(self, filename):
        """
        调用play(sox)命令播放mp3 适配termux
        :param filename:
        :return:
        """
        print("sox play...")
        try:
            ret = os.system("play"+filename)
            return ret
        except Exception:
            return 1

    def play(self, filename):
        """
        音频 播放
        :param filename: 音频文件名称
        :return: null
        """

        is_play_success = self.play_with_sox(filename)
        print("is_play_success is " + str(is_play_success))
        if is_play_success == 0:
            return 0

        if filename.startswith("/") or filename.startswith("./"):
            None
        else:
            filename = "./" + filename
        print(filename)
        try:
            playsound(filename)
        except:
            Play_mp3.play(filename)

