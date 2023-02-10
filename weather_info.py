#-*- coding:utf-8 -*-

import requests
import json

class weather_info(object):

    url="https://restapi.amap.com/v3/weather/weatherInfo"
    city_code = "441900"
    key = "003bed47b58ce28408e3ee5377xx2cec"
    extensions="all"
    output="JSON"


    def __init__(self, citycode="441900", extensions="all"):
        self.city_code=citycode
        self.extensions=extensions

    def struct_info(self):
        payload = {
            "city": self.city_code,
            "key": self.key,
            "extensions": self.extensions,
            "output": self.output
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        response = requests.request("POST", self.url, headers=headers, data=payload)
        print (response.text)

        return response.text

    def text_info(self):
        weather_info = self.struct_info()
        weather_json = json.loads(weather_info)

        if(weather_json['status']!="1" or len(weather_json['forecasts'][0]['casts'])<3):
            return "天气获取失败，请稍后再试。"

        weather_report_time = "天气预报时间 {0},,,".format(weather_json['forecasts'][0]['reporttime'][0:10])

        weather_text_today = "{0} 今日天气 {1}转{2}, 最低气温{3}度，最高气温{4}度, {5}风转{6}风, 风力{7}级到{8}级.".format(weather_json['forecasts'][0]['city'],
                                                  weather_json['forecasts'][0]['casts'][0]['dayweather'],
                                                  weather_json['forecasts'][0]['casts'][0]['nightweather'],
                                                  weather_json['forecasts'][0]['casts'][0]['nighttemp'],
                                                  weather_json['forecasts'][0]['casts'][0]['daytemp'],
                                                  weather_json['forecasts'][0]['casts'][0]['daywind'],
                                                  weather_json['forecasts'][0]['casts'][0]['nightwind'],
                                                  weather_json['forecasts'][0]['casts'][0]['daypower'],
                                                  weather_json['forecasts'][0]['casts'][0]['nightpower'])

        weather_text_tomorrow = "{0} 明日天气 {1}转{2}, 最低气温{3}度，最高气温{4}度, {5}风转{6}风, 风力{7}级到{8}级.".format("",
                                                  weather_json['forecasts'][0]['casts'][1]['dayweather'],
                                                  weather_json['forecasts'][0]['casts'][1]['nightweather'],
                                                  weather_json['forecasts'][0]['casts'][1]['nighttemp'],
                                                  weather_json['forecasts'][0]['casts'][1]['daytemp'],
                                                  weather_json['forecasts'][0]['casts'][1]['daywind'],
                                                  weather_json['forecasts'][0]['casts'][1]['nightwind'],
                                                  weather_json['forecasts'][0]['casts'][1]['daypower'],
                                                  weather_json['forecasts'][0]['casts'][1]['nightpower'])

        weather_text_day_after_tomorrow = " {0} 后日天气 {1}转{2}, 最低气温{3}度，最高气温{4}度, {5}风转{6}风, 风力{7}级到{8}级.".format("",
                                                  weather_json['forecasts'][0]['casts'][2]['dayweather'],
                                                  weather_json['forecasts'][0]['casts'][2]['nightweather'],
                                                  weather_json['forecasts'][0]['casts'][2]['nighttemp'],
                                                  weather_json['forecasts'][0]['casts'][2]['daytemp'],
                                                  weather_json['forecasts'][0]['casts'][2]['daywind'],
                                                  weather_json['forecasts'][0]['casts'][2]['nightwind'],
                                                  weather_json['forecasts'][0]['casts'][2]['daypower'],
                                                  weather_json['forecasts'][0]['casts'][2]['nightpower'])
        weather_text = weather_report_time+weather_text_today+weather_text_tomorrow+weather_text_day_after_tomorrow
        return weather_text







