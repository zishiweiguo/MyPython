# -*- coding: utf-8 -*-
# @Date    : 2019/11/19
# @Author  : xuchao
# @File    : getCityInfo.py
import requests
from bs4 import BeautifulSoup

def getCity():
    url = 'http://www.mca.gov.cn/article/sj/xzqh/2019/2019/201911051008.html'
    html = requests.get(url)
    # html.encoding = 'utf-8'
    soup = BeautifulSoup(html.text, 'html.parser', from_encoding='utf-8')
    trs = soup.find_all('tr', attrs={'height': 19, 'style': 'mso-height-source:userset;height:14.25pt'})

    provs = []
    citys = []
    countys = []

    for tr in trs:
        tds = tr.find_all('td', attrs={'class': 'xl7027502'})  # 省 市
        if len(tds) == 0:
            tds = tr.find_all('td', attrs={'class': 'xl7127502'})  # 区 县
            code = tds[0].get_text()
            name = tds[1].get_text().strip()
            countys.append({'code': code, 'name': name, 'level': 3})
        else:
            code = tds[0].get_text()
            name = tds[1].get_text().strip()
            span = tds[1].find('span')
            if span == None:
                provs.append({'code': code, 'name': name, 'level': 1})
            else:
                citys.append({'code': code, 'name': name, 'level': 2})

    dict = []
    for prov_dict in provs:
        key = prov_dict['code'][0:2]
        count = 0;
        for city_dict in citys:
            k = city_dict['code'][0:2]
            if k == key:
                count = count + 1
                dict.append(
                    {'prov_code': prov_dict['code'], 'prov_name': prov_dict['name'], 'city_code': city_dict['code'],
                     'city_name': city_dict['name']})
        if count == 0:
            dict.append({'prov_code': prov_dict['code'], 'prov_name': prov_dict['name'], 'city_code': prov_dict['code'],
                         'city_name': prov_dict['name']})

    for d in dict:
        key = d['city_code'][0:4]
        count = 0
        for county_dict in countys:

            if d['prov_code'] == d['city_code'] and d['city_code'][0:2] == county_dict['code'][0:2]:
                print('{},{},{},{},{},{}'.format(d['prov_code'], d['prov_name'], d['city_code'], d['city_name'],
                                                 county_dict['code'], county_dict['name']))
            else:
                k = county_dict['code'][0:4]
                if k == key or (k == '4690' and key == '4604'): # 海南省 儋州市 地域代码特例
                    count = count + 1
                    print('{},{},{},{},{},{}'.format(d['prov_code'], d['prov_name'], d['city_code'], d['city_name'],
                                                     county_dict['code'], county_dict['name']))
        if count == 0:
            print('{},{},{},{},{},{}'.format(d['prov_code'], d['prov_name'], d['city_code'], d['city_name'],
                                             d['city_code'], d['city_name']))


if __name__ == "__main__":
    getCity()
