# -*- coding: utf-8 -*-
# @Date    : 2020/12/1
# @Author  : xuchao
# @File    : calendar.py

import requests


# json个数
# {"animal":"鼠","avoid":"装修.开业.开工.安床.出行.安葬.上梁.开张.旅游.修坟.赴任.破土.修造.祈福.祭祀.开市.纳畜.启钻.伐木.盖屋.经络.造桥.筑堤","cnDay":"五","day":"1","desc":"元旦","gzDate":"己酉","gzMonth":"戊子","gzYear":"庚子","isBigMonth":"","lDate":"十八","lMonth":"十一","lunarDate":"18","lunarMonth":"11","lunarYear":"2020","month":"1","oDate":"2020-12-31T16:00:00.000Z","status":"1","suit":"搬家.结婚.入宅.领证.订婚.入学.求嗣.纳财.捕捉.嫁娶.纳采.移徙.竖柱.栽种.斋醮.求财.开仓","term":"","type":"h","value":"元旦","year":"2021"}


# url  https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?query=2021年2月&co=&resource_id=39043&ie=utf8&oe=gbk&format=json&tn=wisetpl


# "status": "2"  班
# "status": "1"  休
# 没有 status 则正常

def query(date_str, save_path):
    f = open(save_path, mode='w', encoding=" utf-8 ")
    m = 2
    for n in range(0, 4):
        url = "https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?query=%s年%d月&co=&resource_id=39043&ie=utf8&oe=gbk&format=json&tn=wisetpl" % (
            date_str, m)
        print(url)
        resp = requests.get(url)
        json = resp.json()
        if json['status'] == '0':
            json_data = json['data'][0]['almanac']

            for i in range(0, len(json_data)):
                data = json_data[i]
                # 年，月，日，星期，状态，生肖，阴历年，阴历月，阴历日
                record = '%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (
                    data['year'], data['month'], data['day'], data['cnDay'], status(data), data['animal'],
                    data['lunarYear'], data['lunarMonth'], data['lunarDate'])
                f.write(record)
        m = m+3
    f.close()


def status(v):
    if 'status' in v:
        status = v['status']
        if status == '1':
            return '休'
        elif status == '2':
            return '班'
    else:
        return '正常'


if __name__ == "__main__":
    date_str = '2021'
    save_path = '2021.txt'
    query(date_str, save_path)

