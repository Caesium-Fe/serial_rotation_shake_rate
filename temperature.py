import re

import serial
import matplotlib.pyplot as plt
import numpy as np
import time
from Log import Log
import serial.tools.list_ports


class SerialPortTemperature:

    def __init__(self):
        # 日志开始记录
        Log.logger.info("start")
        # 串口名称
        self.port = 'COM5'
        # 波特率
        # self.baudrate = 9600
        self.baudrate = 115200
        # 设置串口
        self.ser1 = self.init_serial()

        # 温度指令
        self.datahex = bytes.fromhex('01')

        # 写入默认指令 温度没有默认指令
        # self.write_order()

    def init_serial(self):
        try:
            ser = serial.Serial(self.port, self.baudrate, timeout=2)
            return ser
        except Exception as err:
            Log.logger.exception("No port is " + str(self.port))
            prot = self.get_port_name()
            Log.logger.info("No port is " + str(prot))

    @staticmethod
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

    # def write_order(self):
    #     self.ser1.write(self.datahex_1)
    #     self.ser1.write(self.datahex_2)

    def get_port_data(self):

        num1 = None
        try:
            if not self.ser1.isOpen:
                self.ser1.open()
            # ser1.write(datahex_1)
            self.ser1.write(self.datahex)
            # if not ser2.isOpen:
            #     ser2.open()
            time.sleep(1)
            # b_num1 = ser1.inWaiting()
            # b_num1 = ser1.readall()
            b_num1 = self.ser1.readline(5)
            num1 = int.from_bytes(b_num1[:-1], 'big')
            num1 = (num1 - 1000) / 10
            Log.logger.info(str(num1))
            return num1
        except Exception as e:
            # print(e)
            Log.logger.exception("No port is " + str(self.ser1.port))
            return 0
            # print(str(ser1.port) + " is something wrong!")


if __name__ == '__main__':
    displace_obj = SerialPortTemperature()
    while True:
        displace_obj.get_port_data()
