import json
import os
import pandas as pd
import matplotlib.pyplot as plt
import heads


def read(i="msg.json"):
    f = open(i, 'r+', encoding='utf-8')
    a = f.read()
    f.close()
    a = json.loads(a)
    return a


def read1(i):
    f = open(i, 'r+', encoding='utf-8')
    a = f.read()
    f.close()
    a = json.loads(a)
    return a


def display(**kwargs):  # 字典解析
    for key in kwargs:
        print(key, kwargs[key], "  ", end="")
    print("\n", end="")


def get_type(total, *args):
    direct_flight = []
    stop_flight = []
    transit_flight = []
    calculate = []
    f_number = []
    for num in range(0, total):
        flight_info = args[num]['legs']
        if len(flight_info) == 1:
            if flight_info[0]['flight']['stopInfo'] is not None:
                price = flight_info[0]['characteristic']['lowestPrice']
                number = flight_info[0]['flight']['flightNumber']
                f_number.append(number)
                stop_flight.append(price)
                calculate.append(num)
            else:
                price = flight_info[0]['characteristic']['lowestPrice']
                number = flight_info[0]['flight']['flightNumber']
                f_number.append(number)
                direct_flight.append(price)
                calculate.append(num)
        else:
            price = args[num]['transitPrice']
            number = flight_info[0]['flight']['flightNumber']
            f_number.append(number)
            transit_flight.append(price)
            calculate.append(num)
    return direct_flight, stop_flight, transit_flight, calculate, f_number


def get_flight_id(index, *args):
    flight_id = args[0]['flightId']
    print(flight_id)


def details(*args):
    direct_all = []
    transit_all = []
    for i in args:
        info = {}
        if len(i['legs']) == 1:
            legs = i['legs'][0]
            f_light = legs['flight']
            info['Airline:'] = f_light['airlineName']
            info['FlightNumber:'] = f_light['flightNumber']
            info['CraftTypeName'] = f_light['craftTypeName']
            info['DepartureDate:'] = f_light['departureDate'][-8:-3]
            info['ArrivalDate:'] = f_light['arrivalDate'][-8:-3]
            info['LowestPrice'] = legs['characteristic']['lowestPrice']
            info['PunctualityRate:'] = f_light['punctualityRate']
            if f_light['sharedFlightNumber'] is not None:
                info['SharedFlightNumber'] = f_light['sharedFlightNumber']
            if len(info['SharedFlightNumber']) == 0:
                info.pop('SharedFlightNumber')
            if len(info['PunctualityRate:']) == 0:
                info.pop('PunctualityRate:')
            # print(type(info['SharedFlightNumber']))
            direct_all.append(info)

        else:
            for l in i['legs']:
                dic = {}
                f_light1 = l['flight']
                dic['Airline:'] = f_light1['airlineName']
                dic['FlightNumber:'] = f_light1['flightNumber']
                dic['CraftTypeName'] = f_light1['craftTypeName']
                dic['DepartureDate:'] = f_light1['departureDate']  # [-8:-3]
                dic['ArrivalDate:'] = f_light1['arrivalDate']  # [-8:-3]
                dic['TotalPrice:'] = i['transitPrice']
                dic['PunctualityRate:'] = f_light1['punctualityRate']
                if len(dic['PunctualityRate:']) == 0:
                    dic.pop('PunctualityRate:')
                transit_all.append(dic)

    return direct_all, transit_all


def display_details(*args):
    for item in args:
        display(**item)


def f_get(path):
    x = []
    y = []
    for i in os.listdir(path):
        flight = read(path+'/'+i)['data']['routeList']
        filename = i.split("#")[1].split(".")[0]
        # print(type(flight))
        total = len(flight)
        a = get_type(total, *flight)[0]+get_type(total, *flight)[1]+get_type(total, *flight)[2]
        x.append(a)
        y.append(filename)
        # print(a)
    return x, y


# 输出格式化信息
def show_all(path):
    for i in os.listdir(path):
        flight = read(path+'/'+i)['data']['routeList']
        total = len(flight)
        display_details(*details(*flight)[0])
        print("******")


def draw(filename, flight_list, picture_name="N/A"):
    b = f_get(filename)
    b1 = b[0]
    total = len(flight_list)
    start = 65
    dic = {}

    for i in b[0]:
        dic[chr(start)] = i
        start = start + 1

    t = get_type(total, *flight_list)[4]
    df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in dic.items()]))

    df = df.T
    df.index = b[1]
    # print(t)
    # print(total)
    # print(df)
    df.columns = t
    df.index.name = "Times"
    df.columns.name = "Flight Number"
    df.plot(title=picture_name)
    plt.ylabel("Price")
    plt.savefig(picture_name+".png", dpi=300)
    # plt.show()
