from PyQt5.QtCore import QThread, pyqtSignal
import time


# class globalData:
#     data1_list = []
#     data2_list = []
#     data3_list = []
#     data4_list = []


class updateData1Thread(QThread):
    data1 = pyqtSignal(list)

    def __init__(self, parent):
        super(updateData1Thread, self).__init__()
        self.parent = parent

    def run(self):
        i = 0
        data1_list = []
        data2_list = []
        while True:
            data1_list.append(i)
            data2_list.append(i)
            if len(data1_list) > 10:
                data1_list = data1_list[-10:]
                data2_list = data2_list[-10:]
            self.data1.emit([data1_list, data2_list])

            # print("1  " + str(i))
            time.sleep(0.5)
            i += 1
        pass


class updateData2Thread(QThread):
    data2 = pyqtSignal(list)

    def __init__(self, parent):
        super(updateData2Thread, self).__init__()
        self.parent = parent

    def run(self):
        i = 0
        data3_list = []
        data4_list = []
        while True:
            data3_list.append(i)
            data4_list.append(i)
            if len(data3_list) > 10:
                data3_list = data3_list[-10:]
                data4_list = data4_list[-10:]
            self.data2.emit([data3_list, data4_list])

            # print("1  " + str(i))
            time.sleep(0.5)
            i += 1
        pass


class GetData1Thread(QThread):
    data1 = pyqtSignal(int)

    def __init__(self, parent):
        super(GetData1Thread, self).__init__()
        self.parent = parent

    def run(self):
        i = 0
        while i < 20:
            self.data1.emit(i)
            globalData.data1_list.append(i)
            # print("1  " + str(i))
            time.sleep(0.5)
            i += 1
        pass


class GetData2Thread(QThread):
    data2 = pyqtSignal(int)

    def __init__(self, parent):
        super(GetData2Thread, self).__init__()
        self.parent = parent

    def run(self):
        i = 0
        while i < 20:
            self.data2.emit(i)
            globalData.data2_list.append(i)
            # print("2  " + str(i))
            time.sleep(0.5)
            i += 1
        pass


class GetData3Thread(QThread):
    data3 = pyqtSignal(int)

    def __init__(self, parent):
        super(GetData3Thread, self).__init__()
        self.parent = parent

    def run(self):
        i = 0
        while True:
            self.data3.emit(i)
            globalData.data3_list.append(i)
            # print("3  " + str(i))
            time.sleep(0.5)
            i += 1
        pass


class GetData4Thread(QThread):
    data4 = pyqtSignal(int)

    def __init__(self, parent):
        super(GetData4Thread, self).__init__()
        self.parent = parent

    def run(self):
        i = 0
        while True:
            # print(globalData.data4_list)
            self.data4.emit(i)
            globalData.data4_list.append(i)
            # print("4  " + str(i))
            time.sleep(0.5)
            i += 1
        pass


class UpdatePainting(QThread):
    data_list = pyqtSignal(list)

    def __init__(self, parent):
        super(UpdatePainting, self).__init__()
        self.parent = parent

    def run(self):
        while True:
            # print(globalData.data1_list)
            a, b, c, d = len(globalData.data1_list), len(globalData.data2_list), len(globalData.data3_list), len(
                globalData.data4_list)
            if a > 10:
                globalData.data1_list = globalData.data1_list[-10:]
                globalData.data2_list = globalData.data2_list[-10:]
                globalData.data3_list = globalData.data3_list[-10:]
                globalData.data4_list = globalData.data4_list[-10:]
                four_list = [[globalData.data1_list], [globalData.data2_list], [globalData.data3_list],
                             [globalData.data4_list]]
                self.data_list.emit(four_list)
            else:
                four_list = [[globalData.data1_list], [globalData.data2_list], [globalData.data3_list],
                             [globalData.data4_list]]
                self.data_list.emit(four_list)
