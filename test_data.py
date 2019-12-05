import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tools
import os
import seaborn as sns

plt.rcParams['figure.figsize'] = (12.0, 8.0)  # 设置figure_size尺寸
plt.rcParams['image.interpolation'] = 'nearest'  # 设置 interpolation style
plt.rcParams['image.cmap'] = 'gray'  # 设置 颜色 style

fil = os.path.abspath("Flights")
fil2 = os.path.abspath('Tjnn')
flight = tools.read("Flights/"+os.listdir(fil)[30])['data']['routeList']
flight2 = tools.read("Tjnn/"+os.listdir(fil2)[0])['data']['routeList']
# total = len(flight)
# start = 65
# a = tools.f_get(fil)
# b = tools.f_get(fil2)
# a1 = a[0]
# dic = {}
# for i in a[0]:
#     dic[chr(start)] = i
#     start = start + 1
#
# t = tools.get_type(total, *flight)[4]
# df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in dic.items()]))
# # df = pd.DataFrame(dic)
#
# df = df.T
# x = pd.date_range(start='20191109', freq='30s', periods=len(df.index))
# dates = pd.date_range('20130101', periods=6)
# f = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
# df.index = a[1]
# df.columns = t
#
# df.plot()
# plt.savefig('No1.png', dpi=300)
# plt.show()


# def draw(filename, flight_list):
#     b = tools.f_get(filename)
#     b1 = b[0]
#     total = len(flight_list)
#     start = 65
#     dic = {}
#
#     for i in b[0]:
#         dic[chr(start)] = i
#         start = start + 1
#
#     t = tools.get_type(total, *flight_list)[4]
#     df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in dic.items()]))
#     df = df.T
#     df.index = b[1]
#
#     df.columns = t
#     df.plot()
#     plt.show()
tools.draw(fil, flight, "PEK^PKX-NNG2020-01-11")
tools.draw(fil2, flight2, "TSN-NNG2020-01-11")
