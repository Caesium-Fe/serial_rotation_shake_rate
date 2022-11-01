from PyQt5.QtCore import QThread, pyqtSignal, QMutex, QWaitCondition
import time

import random
import numpy as np

from RotationAndShaking import GetTxtData
from displacement import SerialPortDisplace
from temperature import SerialPortTemperature

global data1_list, data2_list
data1_list, data2_list = [], []
global data3_list, data4_list
data3_list, data4_list = [], []


# class globalData:
#     data1_list = []
#     data2_list = []
#     data3_list = []
#     data4_list = []


class updateData1Thread(QThread):
    data1 = pyqtSignal(list)

    def __init__(self, parent):
        super(updateData1Thread, self).__init__()
        self._isPause = False
        self.mutex = QMutex()
        self.cond = QWaitCondition()
        self.parent = parent
        self.data_obj = GetTxtData()

    def pause(self):
        self._isPause = True

    def resume(self):
        self._isPause = False
        self.cond.wakeAll()

    def run(self):
        # data1_list = []
        # data2_list = []
        global data1_list
        global data2_list
        while True:
            self.mutex.lock()
            if self._isPause:
                self.cond.wait(self.mutex)
            i1 = self.data_obj.getShakingData()
            i2 = self.data_obj.getRotationData()
            # data1_list.append(i)
            # data2_list.append(i)
            data1_list.append(i1)
            data2_list.append(i2)
            # if len(data1_list) > 20:
            data5_list = data1_list[-10:]
            data6_list = data2_list[-10:]
            self.data1.emit([data5_list, data6_list])

            # print("1  " + str(i))
            time.sleep(0.1)
            # if i > 500:
            #     return
            self.mutex.unlock()
        pass


class updateData2Thread(QThread):
    data2 = pyqtSignal(list)

    def __init__(self, parent):
        super(updateData2Thread, self).__init__()
        self._isPause = False
        self.mutex = QMutex()
        self.cond = QWaitCondition()
        self.parent = parent
        self.displace_obj = SerialPortDisplace()
        self.temperature_obj = SerialPortTemperature()

    def pause(self):
        self._isPause = True

    def resume(self):
        self._isPause = False
        self.cond.wakeAll()

    def run(self):
        # j = 0
        # global j
        # data3_list = []
        # data4_list = []
        global data3_list
        global data4_list
        while True:
            self.mutex.lock()
            if self._isPause:
                self.cond.wait(self.mutex)
            temp = self.temperature_obj.get_port_data()
            disp = self.displace_obj.get_port_data()
            if temp != -100 and disp != 999:
                data3_list.append(temp)
                data4_list.append(disp)
                # if len(data3_list) > 10:
                data7_list = data3_list[-10:]
                data8_list = data4_list[-10:]
                self.data2.emit([data7_list, data8_list])

            # print("1  " + str(i))
            time.sleep(0.1)
            # if j > 500:
            #     return
            self.mutex.unlock()
        pass


class updateData3Thread(QThread):
    data3 = pyqtSignal(list)

    def __init__(self, parent):
        super(updateData3Thread, self).__init__()
        self.parent = parent

    def run(self):
        # j = 0
        # global j
        # # data3_list = []
        # # data4_list = []
        # global data3_list
        # global data4_list
        # while True:
        #     data3_list.append(j)
        #     data4_list.append(j)
        #     # if len(data3_list) > 10:
        #     data7_list = data3_list[-10:]
        #     data8_list = data4_list[-10:]
        self.data3.emit([data1_list, data2_list, data3_list, data4_list])
        return
            # print("1  " + str(i))
        #     time.sleep(0.1)
        #     j += 1
        # pass

