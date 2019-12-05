from bs4 import BeautifulSoup
import requests
from threading import Timer
import heads
import tools
import os
import time
import json
import sys

dcity = "北京"
acity = "南宁"
date = "2020-01-11"
fil = os.path.abspath("Flights")
fil2 = os.path.abspath("Tjnn")
# dcity = input("出发地:")
# acity = input("到达地:")
# date = input("日期 yyyy-mm-dd:")
url3 = "https://flights.ctrip.com/itinerary/api/12808/products"
# payload = {
#     "flightWay": "Oneway",  # 飞行方式 单向的 固定参数
#     "classType": "ALL",
#     "hasChild": "false",
#     "hasBaby": "false",
#     "searchIndex": 1,
#     "mkt_header": "bdnm",  # 固定参数
#     "airportParams": [
#         {
#             "dcity": heads.city.get(dcity),  # 起点
#             "acity": heads.city.get(acity),  # 终点
#             "dcityname": dcity,  # 起点名称 没有起作用
#             "acityname": acity,  # 终点名称 设置错误 暂时也是返回的正确数据
#             "date": date  # 请求时间
#         }
#     ]
# }


def load():
    html = requests.post(url3, headers=heads.header, json=heads.payload)
    data = json.loads(html.text)
    # d = os.getcwd()
    t = time.strftime("%Y%m%d#%H%M%S", time.localtime())
    path = os.path.abspath('Flights')
    path = os.path.join(path, str(t)+'.json')
    f = open(path, 'w', encoding='utf-8')
    f.write(html.text)
    f.close()
    s = Timer(300, load)
    s.start()


def load1():
    html = requests.post(url3, headers=heads.header, json=heads.payload)
    data = json.loads(html.text)
    # d = os.getcwd()
    t = time.strftime("%Y%m%d#%H%M%S", time.localtime())
    path = os.path.abspath('Flights')
    path = os.path.join(path, str(t)+'.json')
    f = open(path, 'w', encoding='utf-8')
    f.write(html.text)
    f.close()

def load2():
    html = requests.post(url3, headers=heads.header, json=heads.payload1)
    data = json.loads(html.text)
    # d = os.getcwd()
    t = time.strftime("%Y%m%d#%H%M%S", time.localtime())
    path = os.path.abspath('Tjnn')
    path = os.path.join(path, str(t)+'.json')
    f = open(path, 'w', encoding='utf-8')
    f.write(html.text)
    f.close()
# html = requests.post(url3, headers=heads.header, json=payload)
# data = json.loads(html.text)
# f = open('msg.json', 'w', encoding='utf-8')
# f.write(html.text)
# f.close()
# f = open('msg.json', 'r+', encoding='utf-8')
# a = f.read()
# f.close()
# a = json.loads(a)
# flight = a['data']['routeList']

flight = tools.read()['data']['routeList']

total = len(flight)
# print("总航班数", total)  # ['legs']是航段，长度为二即有中转
msg = flight[0]['legs'][0]['flight']  # 中专信息在msg['stopInfo'] <class 'list'>
# print(type(msg))
# print(type(flight))
# price = flight[0]['legs'][0]['characteristic']['lowestPrice']  # 最低价

# # dic{"a":{}}
# # print(heads.city.get(input()))
# # 755行
# for b in range(0, len(flight)):
#     print(flight[y]['legs'][0]['flightId'])
#     y = y+1
#     get_flight_id(b, *flight[b]['legs'])
# for x in tools.details(*flight):
#      tools.display_details(*x)
#      print("*******************")
# tools.display_details(*tools.details(*flight)[0])
# lis = tools.get_type(total, *flight)[0]
# print(min(lis))
# print(lis.index(min(lis)))
load1()
load2()
# time.sleep(1800)
# tools.show_all(fil2)
# tools.f_get(fil)[0]
# print("ok at "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# os._exit(0)
