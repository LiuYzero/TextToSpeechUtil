# TextToSpeechUtil

## 功能简介

a. 转换文字为mp3音频文件并保存到当前文件夹

b. 播放mp3音频文件

## 系统支持
支持windows、linux、termux(手机端模拟器)

已验证环境 Windows10, Ubuntu22.04, Termux-Ubuntu

## 依赖

### tts服务API
利民吧
http://www.liminba.com/tool_api/tts.php

### windowsh环境依赖
python模组 requests、playsound、play_mp3
安装命令

```python
pip install requests playsound play_mp3
```

### linux环境依赖
python模组 requests、playsound、play_mp3
安装命令

```python
pip install requests playsound play_mp3
```
软件依赖 sox libsox-fmt-all
安装命令

```shell
# Ubuntu
apt install sox libsox-fmt-all -y
```

### termux环境依赖
python模组 requests、playsound、play_mp3
安装命令

```python
pip install requests playsound play_mp3
```
软件依赖 sox libsox-fmt-all
安装命令

```shell
# Ubuntu
apt install sox libsox-fmt-all -y
```



## 测试

```python
python test.py
```

