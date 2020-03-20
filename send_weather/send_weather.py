# -*- coding: utf-8 -*-
# @Date    : 2019/9/30
# @Author  : xuchao
# @File    : send_weather.py

import requests
from wxpy import Bot


def get_weather() :
    url = 'http://t.weather.sojson.com/api/weather/city/101010200'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'
    }

    # 请求Weather API并拿到服务器返回的数据
    rep = requests.get(url, headers = header)
    rep.encoding = "utf-8"
    result = ''
    weather = rep.tex

    # 解析服务器返回的数据，具体可参考weather.json文件
    index_cityInfo = weather.find("cityInfo")
    index_cityId = weather.find("cityId")
    index_shidu = weather.find("shidu")
    index_pm25 = weather.find("pm25")
    index_pm10 = weather.find("pm10")
    index_quality = weather.find("quality")
    index_wendu = weather.find("wendu")
    index_ganmao = weather.find("ganmao")
    index_forecast = weather.find("forecast")
    index_ymd = weather.find("ymd", index_forecast)
    index_week = weather.find("week", index_forecast)
    index_sunset = weather.find("sunset", index_forecast)
    index_high = weather.find("high", index_forecast)
    index_low = weather.find("low", index_forecast)
    index_fx = weather.find("fx", index_forecast)
    index_fl = weather.find("fl", index_forecast)
    index_aqi = weather.find("aqi", index_forecast)
    index_type = weather.find("type", index_forecast)
    index_notice = weather.find("notice", index_forecast)

    result = '今日天气预报' + '\n' \
        + weather[index_ymd + 6:index_week - 3] + " " \
        + weather[index_week + 7:index_fx - 3] + " " \
        + weather[index_cityInfo + 19:index_cityId - 3] + '\n' \
        + "天气: " + weather[index_type + 7:index_notice - 3] + " " \
        + weather[index_fx + 5:index_fl - 3] \
        + weather[index_fl + 5:index_type - 3] + '\n' \
        + "温度范围:" + weather[index_low + 9:index_sunset - 3] + " ~" \
        + weather[index_high + 10:index_low - 3] + '\n' \
        + "污染指数: PM2.5:" + weather[index_pm25 + 6:index_pm10 - 1] + "" \
        + "PM10:" + weather[index_pm10 + 6:index_quality - 1] + " " \
        + "AQI:" + weather[index_aqi + 5:index_ymd - 2] + '\n' \
        + "空气质量:" + weather[index_quality + 10:index_wendu - 3] + '\n' \
        + "当前温度:" + weather[index_wendu + 8:index_ganmao - 3] + " " \
        + "空气湿度:" + weather[index_shidu + 8:index_pm25 - 3] + '\n' \
        + weather[index_notice + 9:weather.find('}', index_notice) - 1]

    print(result)
    return result;


# 初始化机器人，扫码登陆微信，适用于Windows系统
bot = Bot()

# Linux系统，执行登陆请调用下面的这句
# bot = Bot(console_qr=2, cache_path="botoo.pkl")

# 调用get_weather函数
GW = get_weather()
# 填入你朋友的微信昵称，注意这里不是备注，也不是微信帐号
my_friend = bot.friends().search(u'蔡芝芝')[0]
# 发送微信消息
my_friend.send(u"早上好Y(^o^)Y，这里是今日份的天气信息请查收!")
my_friend.send(GW)
my_friend.send(u"Have a Nice Day!")

# 每隔86400秒（1天），发送1次
# t = Timer(86400, auto_send)
# t.start()