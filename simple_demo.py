# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import requests
import base64
from playsound import playsound
import Play_mp3
import os

def covert_text_to_mp3(text):
    url = "http://www.liminba.com/tool_api/tts.php"

    payload = {
        "type": "tn",
        "spd": 5,
        "pit": 5,
        "vol": 5,
        "dt": 5,
        "peer": 4115,
        "tex": "Looking for the current version of Winamp? While we’re working hard on the new Winamp, we recommend downloading the latest desktop version here, as we guarantee it is safe for you to use."
    }
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload)
    # print (response.text)

    audio_content_base64 = filter_response(response)
    # print (audio_content_base64)

    write_mp3_by_base64_content(audio_content_base64)
    
    try:
       play("foo.mp3")
    except:
       print ("play faild")


def filter_response(response):
    default_format="data:audio/x-mpeg;base64,"
    if response.text.find(default_format) != -1:
        print ("is audio in base64")
        return response.text.replace(default_format,"")
    else:
        print ("not audio in base64")
        return ""

def write_mp3_by_base64_content(audio_content_base64, filename="foo.mp3"):
    with open(filename,"wb") as temp_file:
        temp_file.write(base64.b64decode(audio_content_base64))

def play_with_sox(filename):
    print ("sox play...")
    try:
        os.system("play foo.mp3")
        return 0
    except :
        return 1


def play(filename):
    
    is_play_success = play_with_sox("foo.mp3")
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

def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')
    covert_text_to_mp3("")

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
