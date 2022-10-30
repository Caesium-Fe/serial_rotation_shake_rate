from PyQt5.QtCore import QThread, pyqtSignal, QMutex, QWaitCondition
import time

import random
import numpy as np

from displacement import SerialPortDisplace
from temperature import SerialPortTemperature

global i, j
i, j = 0, 0

global data1_list, data2_list
data1_list, data2_list = [], []
global data3_list, data4_list
data3_list, data4_list = [], []
i, j = 0, 0


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

    def pause(self):
        self._isPause = True

    def resume(self):
        self._isPause = False
        self.cond.wakeAll()

    def run(self):
        global i
        # data1_list = []
        # data2_list = []
        global data1_list
        global data2_list
        while True:
            # i = 0
            # i1 = i
            self.mutex.lock()
            if self._isPause:
                self.cond.wait(self.mutex)
            i1 = np.around(random.uniform(10, 100), 2)
            i2 = np.around(random.uniform(10, 100), 2)
            # data1_list.append(i)
            # data2_list.append(i)
            data1_list.append(i1)
            data2_list.append(i2)
            # if len(data1_list) > 20:
            data5_list = data1_list[-20:]
            data6_list = data2_list[-20:]
            self.data1.emit([data5_list, data6_list])

            # print("1  " + str(i))
            time.sleep(0.1)
            i += 1
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
            data3_list.append(self.displace_obj.get_port_data())
            data4_list.append(self.temperature_obj.get_port_data())
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
