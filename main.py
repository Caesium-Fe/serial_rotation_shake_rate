import re

import serial
import matplotlib.pyplot as plt
import numpy as np
import time
from Log import Log
import serial.tools.list_ports


def init_serial(port_name, btl):
    try:
        ser = serial.Serial(port_name, btl, timeout=2)
        return ser
    except Exception as err:
        Log.logger.exception("No port is " + str(port_name))
        prot = get_port_name()
        Log.logger.info("No port is " + str(prot))
        ser.close()


def get_port_name():
    port_list = list(serial.tools.list_ports.comports())
    if len(port_list) <= 0:

    # if len(port_list) <= 0:
        Log.logger.info("The Serial port can't find!")
        # wx.MessageBox("The Serial port can't find!", 'Info', wx.OK | wx.ICON_INFORMATION)
    else:
        print(len(port_list))
        # print(port_list[0].description)
        for p in port_list:
            if 'USB Serial Port'.lower() in p.description.lower():
                des = p.description
                r = re.search('\(([0-9z-zA-Z]*)\)', des, re.I)
                if r:
                    return r.group(1)

Log.logger.info("start")

# def open_true_fail(ser):
#     if ser.isOpen():
#         print(ser.name + "open success!")
#     else:
#         print(ser.name + "open fail!")


# 创建画布
# plt.ion()
# plt.figure(1, figsize=(15.7, 6), dpi=80)

# 串口名称
port = 'COM3'
# ser2.port = 'COM97'
# 波特率
baudrate = 115200

# 设置串口
ser1 = init_serial(port, baudrate)
# ser2 = init_serial()
# ser2.baudrate = 115200
# 接收值大小
# ser1.bytesize = 8
# ser2.bytesize = 8
#
# ser1.parity = serial.PARITY_NONE
# ser2.parity = serial.PARITY_NONE
# ser1.stopbits = 1
# ser2.stopbits = 1
# ser1.timeout = 0.001
# ser2.timeout = 0.001

# ser1.close()
# ser2.close()

# # 判断接口是否正确连接
# open_true_fail(ser1)
# open_true_fail(ser2)

# 接收数据
rotation = []
shake = []
temperature = []

# 循环接收串口值
while True:
    num1 = None
    try:
        if not ser1.isOpen:
            ser1.open()
    # if not ser2.isOpen:
    #     ser2.open()
        time.sleep(0.05)
        num1 = ser1.inWaiting()
    except Exception:
        Log.logger.exception("No port is " + str(ser1.port))
        # print(str(ser1.port) + " is something wrong!")
    # num2 = ser2.inWaiting()
    if num1:
    # if num1 and num2:
        # 解析出来是字符串
        try:
            Log.logger.info("com3's data type is " + type(num1))
            data1 = ser1.read(num1).decode('UTF-8')
        # print(data1)
            Log.logger.info("com3's data type is " + type(data1))
        except Exception:
            ser1.close()
            Log.logger.exception("No port is " + str(ser1.port))
        # 解析出来是二进制
        # data2 = ser2.read(1)
        # intdata = int.from_bytes(data2, byteorder='big', signed=False)
        rotation.append(data1)
        # shake.append(intdata)
        # 清除之前遗留数据
        if len(rotation) > 10:
            rotation = rotation[-10:]
            shake = shake[-10:]
        # 指定x轴y轴数据样式
        # plt.clf()
        # plt.plot(range(len(rotation)), shake, '-r')
        # plt.xticks(range(len(rotation)), rotation)
        # plt.yticks(shake)
        # plt.grid(True)  # 添加网格
        # plt.xlabel('rotation')
        # plt.ylabel('shake')
        # plt.title('rotation_shake_rate')
        # plt.pause(0.1)
        # plt.ioff()
    time.sleep(0.002)
