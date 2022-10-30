#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time      : 2022/9/06 下午 05:00
# @Author   : ghost(fan.xia)
# @Email    : ghost.f.xia@mail.foxconn.com
# File      : fileTableWidget.py


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import matplotlib.pyplot as plt
# import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
# from threading import Thread
# from get_data_threading import updateData1Thread, updateData2Thread
from get_data_threading import updateData1Thread, updateData2Thread, updateData3Thread

# from get_data_threading import GetData3Thread, GetData4Thread

# matplotlib.use("Qt5Agg")


plt.switch_backend('agg')


# global_rotation, global_temperature, global_move, global_shake = int


class FileWidget(QWidget):
    def __init__(self, parent=None):
        super(FileWidget, self).__init__(parent)

    def paintEvent(self, QPaintEvent):
        path = QPainterPath()
        path.setFillRule(Qt.WindingFill)
        path.addRect(3, 3, self.width() - 6, self.height() - 6)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.fillPath(path, QBrush(Qt.white))

        color = QColor(3, 39, 62, 10)

        for i in range(0, 3):
            path.setFillRule(Qt.WindingFill)
            path.addRect(3 - i, 3 - i, self.width() - (3 - i) * 2, self.height() - (3 - i) * 2, )
            color.setAlpha(15)
            painter.setPen(color)
            painter.drawPath(path)


class MyFigure(FigureCanvas):
    def __init__(self, width=3.2, height=2.7, dpi=70):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        super(MyFigure, self).__init__(self.fig)


# def getPortData(port_name):


class FileTableWidget(QWidget):

    def __init__(self, parent=None):
        super(FileTableWidget, self).__init__(parent)
        self.data1Thread = updateData1Thread(self)
        self.data2Thread = updateData2Thread(self)
        self.data3Thread = updateData3Thread(self)
        self.setWindowTitle('')
        self.setObjectName('mainUi')
        self.setMinimumSize(1500, 750)
        # self.setWindowIcon('')
        self.setStyleSheet('''
            QLabel#label{
                color: rgba(51, 51, 51,1);
                font-size:20px;
            }QLabel#label1{
                color: rgba(51, 51, 51,1);
                font-weight: bold;
                font-size:20px;
            }
        ''')
        self.initUi()
        # self.label3.setStyleSheet()
        # self.data1 = pyqtSignal()
        # self.data2 = pyqtSignal()
        # self.data3 = pyqtSignal()
        # self.data4 = pyqtSignal()
        # self.getDatas()
        # self.datathread = GetData1Thread(self)
        # self.datathread.data1.connect(self.update_label3)
        # self.datathread.start()
        # self.data1.connect(lambda: self.update_label3())
        # self.data2.connect(lambda: self.update_label4())
        # self.data3.connect(lambda: self.update_label5())
        # self.data4.connect(lambda: self.update_label6())

    def getDatas(self):
        # datas = [' ', ' ', ' ', ' ']
        # for i in range(3):
        self.pushbutton1.setEnabled(False)
        self.pushbutton2.setEnabled(True)
        self.pushbutton3.setEnabled(False)
        self.pushbutton4.setEnabled(True)
        self.data1Thread.data1.connect(self.update1)
        self.data1Thread.start()
        self.data2Thread.data2.connect(self.update2)
        self.data2Thread.start()

    def pauseDraw(self):
        self.pushbutton1.setEnabled(False)
        self.pushbutton2.setEnabled(False)
        self.pushbutton3.setEnabled(True)
        self.pushbutton4.setEnabled(False)
        self.data1Thread.pause()
        self.data2Thread.pause()

    def resumeDraw(self):
        self.pushbutton1.setEnabled(False)
        self.pushbutton2.setEnabled(True)
        self.pushbutton3.setEnabled(False)
        self.pushbutton4.setEnabled(True)
        self.data1Thread.resume()
        self.data2Thread.resume()
        # try:
        #     self.data1Thread.terminate()
        #     self.data2Thread.terminate()
        # except AttributeError:
        #     self.pushbutton2.setEnabled(True)
        #     pass

    def drawUltimatePic(self):
        self.pushbutton1.setEnabled(False)
        self.pushbutton2.setEnabled(False)
        self.pushbutton3.setEnabled(False)
        self.pushbutton4.setEnabled(False)
        self.data1Thread.pause()
        self.data2Thread.pause()
        self.data3Thread.data3.connect(self.update3)
        self.data3Thread.start()

    def update1(self, arg):
        # print("1  " + str(arg))
        self.label3.setText('Vibration %5s mm/s' % str(arg[0][-1]))
        self.label4.setText('Rotation %5s rad/min' % str(arg[1][-1]))
        print('begin')
        self.figure.axes.cla()
        # self.figure.axes.plot(arg[0], arg[1])
        self.figure.axes.plot(range(len(arg[0])), arg[1])
        self.figure.axes.set_xlabel('Vibration')
        self.figure.axes.set_ylabel('Rotation')
        self.figure.axes.grid(True)
        # self.figure.axes.set_xticks(arg[0])
        # self.figure.axes.set_xticklabels(arg[0])
        self.figure.axes.set_xticks(range(len(arg[0])))
        self.figure.axes.set_xticklabels(arg[0])
        # self.figure.axes.set_yticks(arg[1])
        # self.figure.axes.set_yticklabels(arg[1])
        # self.figure.axes.figure.xticks(range(len(arg[0])), arg[0])
        # plt.xticks(range(len(arg[0])), arg[0])
        # self.figure.axes.set_xticks(arg[0])
        # self.figure.axes.set_xticklabels(arg[0])
        # self.figure.axes.set_xticklabels(arg[0])
        self.figure.axes.figure.canvas.draw()
        self.figure.axes.figure.canvas.flush_events()
        print('end')

    def update2(self, arg):
        self.label5.setText('Temperature %5s ℃' % str(arg[0][-1]))
        self.label6.setText('Displacement %5s mm' % str(arg[1][-1]))
        print('begin')
        self.figure2.axes.cla()
        self.figure2.axes.plot(arg[0], arg[1])
        self.figure2.axes.set_xlabel('Temperature')
        self.figure2.axes.set_ylabel('Displacement')
        self.figure2.axes.grid(True)
        self.figure2.axes.set_xticks(range(len(arg[0])))
        self.figure2.axes.set_xticklabels(arg[0])
        self.figure2.axes.figure.canvas.draw()
        self.figure2.axes.figure.canvas.flush_events()
        print('end')
        # self.label4 = QLabel('转速' + str(self.data2) + 'rad/min', self)

    def update3(self, arg):
        # self.label5.setText('Temperature %5s ℃' % str(arg[0][-1]))
        # self.label6.setText('Displacement %5s mm' % str(arg[1][-1]))
        print('begin')
        self.figure.axes.cla()
        # self.figure.axes.plot(arg[0], arg[1])
        self.figure.axes.plot(range(len(arg[0])), arg[1])
        self.figure.axes.set_xlabel('Vibration')
        self.figure.axes.set_ylabel('Rotation')
        self.figure.axes.grid(True)
        # self.figure.axes.set_xticks(arg[0])
        # self.figure.axes.set_xticklabels(arg[0])
        self.figure.axes.set_xticks(range(len(arg[0])))
        self.figure.axes.set_xticklabels(arg[0], rotation=45)
        # self.figure.axes.set_yticks(arg[1])
        # self.figure.axes.set_yticklabels(arg[1])
        # self.figure.axes.figure.xticks(range(len(arg[0])), arg[0])
        # plt.xticks(range(len(arg[0])), arg[0])
        # self.figure.axes.set_xticks(arg[0])
        # self.figure.axes.set_xticklabels(arg[0])
        # self.figure.axes.set_xticklabels(arg[0])
        self.figure.axes.figure.canvas.draw()
        self.figure.axes.figure.canvas.flush_events()
        print('end')

        print('begin')
        self.figure2.axes.cla()
        self.figure2.axes.plot(arg[2], arg[3])
        self.figure2.axes.set_xlabel('Temperature')
        self.figure2.axes.set_ylabel('Displacement')
        self.figure2.axes.grid(True)
        self.figure2.axes.set_xticks(range(len(arg[2])))
        self.figure2.axes.set_xticklabels(arg[2])
        self.figure2.axes.figure.canvas.draw()
        self.figure2.axes.figure.canvas.flush_events()
        print('end')

    # def update_label5(self, arg):
    #     self.label5.setText('温度 ' + str(arg) + ' ℃')
    #
    # def update_label6(self, arg):
    #     self.label6.setText('位移 ' + str(arg) + ' mm')

    def initUi(self):
        self.label1 = QLabel('深圳市日野精密科技有限公司', self)
        self.label2 = QLabel(self)
        self.label3 = QLabel('Vibration %5s mm/s' % str(0.0), self)
        self.label4 = QLabel('Rotation  %5s rad/min' % str(0.0), self)
        self.label5 = QLabel('Temperature %5s ℃' % str(0.0), self)
        self.label6 = QLabel('Displacement %5s mm' % str(0.0), self)
        self.label1.setObjectName('label1')
        self.label3.setObjectName('label')
        self.label4.setObjectName('label')
        self.label5.setObjectName('label')
        self.label6.setObjectName('label')
        self.pushbutton1 = QPushButton('Start', self)
        self.pushbutton2 = QPushButton('Stop', self)
        self.pushbutton3 = QPushButton('Resume', self)
        self.pushbutton4 = QPushButton('Finish', self)
        self.fileWidget = FileWidget(self)
        self.fileWidget.setObjectName('fileWidget')
        self.fileWidgetlayout = QVBoxLayout(self.fileWidget)
        self.figure = MyFigure(self.width() * 0.1, self.height() * 0.1)
        self.figure.axes.set_xlabel('Vibration')
        self.figure.axes.set_ylabel('Rotation')
        self.figure2 = MyFigure(self.width() * 0.1, self.height() * 0.1)
        self.figure2.axes.set_xlabel('Temperature')
        self.figure2.axes.set_ylabel('Displacement')
        self.fileWidgetlayout.addWidget(self.figure)
        self.fileWidgetlayout.addWidget(self.figure2)
        # self.fileWidgetlayout.setSpacing(50)
        # self.pushbutton.clicked.connect(lambda: self.updatePaint())
        # self.pushbutton = QPushButton('Start', self)
        self.pushbutton1.clicked.connect(lambda: self.getDatas())
        self.pushbutton2.clicked.connect(lambda: self.pauseDraw())
        self.pushbutton3.clicked.connect(lambda: self.resumeDraw())
        self.pushbutton4.clicked.connect(lambda: self.drawUltimatePic())

    def resizeEvent(self, QResizeEvent):
        self.label1.setGeometry(500, 20, 700, 20)
        self.label2.setGeometry(1230, 50, 30, 20)
        self.label3.setGeometry(1200, 110, 200, 30)
        self.label4.setGeometry(1200, 250, 200, 30)
        self.label5.setGeometry(1200, 410, 200, 30)
        self.label6.setGeometry(1200, 550, 200, 30)
        self.fileWidget.setGeometry(50, 50, 1100, 700)
        self.pushbutton1.setGeometry(1200, 650, 60, 30)
        self.pushbutton2.setGeometry(1300, 650, 60, 30)
        self.pushbutton3.setGeometry(1200, 700, 60, 30)
        self.pushbutton4.setGeometry(1300, 700, 60, 30)

    def paintEvent(self, a0: QPaintEvent) -> None:
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    fileTest = FileTableWidget()
    fileTest.show()
    sys.exit(app.exec_())
