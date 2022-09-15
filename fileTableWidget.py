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
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from threading import Thread

matplotlib.use("Qt5Agg")
# plt.switch_backend('agg')

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
    def __init__(self, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        super(MyFigure, self).__init__(self.fig)


def getPortData(port_name):
    pass
# def getPortData(port_name):



class FileTableWidget(QWidget):
    def __init__(self, parent=None):
        super(FileTableWidget, self).__init__(parent)
        self.setWindowTitle('')
        self.setObjectName('mainUi')
        self.setMinimumSize(1400, 700)
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
        # self.label3.setStyleSheet()
        datas = self.getDatas()
        self.initUi(datas)

    def getDatas(self):
        datas = [' ', ' ', ' ', ' ']
        for i in range(3):
            t = Thread(target=getPortData, args=('t1',))
            t.start()
        datas = [' ', ' ', ' ', ' ']
        # for i in range(3):
        #     t = Thread(target=getPortData, args=('t1',))
        #     t.start()
        return datas

    def initUi(self, datas=[' ', ' ', ' ', ' ']):
        self.label1 = QLabel('深圳市日野精密科技有限公司', self)
        self.label2 = QLabel(self)
        self.label3 = QLabel('振动' + datas[0] + 'mm/s', self)
        self.label4 = QLabel('转速' + datas[1] + 'rad/min', self)
        self.label5 = QLabel('温度' + datas[2] + '℃', self)
        self.label6 = QLabel('位移' + datas[3] + 'mm', self)
        self.label1.setObjectName('label1')
        self.label3.setObjectName('label')
        self.label4.setObjectName('label')
        self.label5.setObjectName('label')
        self.label6.setObjectName('label')
        self.pushbutton = QPushButton('Start', self)
        self.fileWidget = FileWidget(self)
        self.fileWidget.setObjectName('fileWidget')
        self.fileWidgetlayout = QVBoxLayout(self.fileWidget)
        self.figure = MyFigure(self.width() * 0.9, self.height() * 0.9)
        self.figure2 = MyFigure(self.width() * 0.9, self.height() * 0.9)
        self.fileWidgetlayout.addWidget(self.figure)
        self.fileWidgetlayout.addWidget(self.figure2)
        self.pushbutton.clicked.connect(lambda: self.updatePaint())

    def resizeEvent(self, QResizeEvent):
        self.label1.setGeometry(500, 20, 700, 20)
        self.label2.setGeometry(1230, 50, 30, 20)
        self.label3.setGeometry(1200, 110, 100, 30)
        self.label4.setGeometry(1200, 250, 100, 30)
        self.label5.setGeometry(1200, 410, 100, 30)
        self.label6.setGeometry(1200, 550, 100, 30)
        self.fileWidget.setGeometry(50, 50, 1050, 600)
        self.pushbutton.setGeometry(1200, 650, 60, 30)

    def paintEvent(self, a0: QPaintEvent) -> None:
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)

    def updatePaint(self, lists=[[1,2,3],[1,2,3],[1,2,3],[1,2,3]]):
        print('begin')
        self.figure.axes.cla()
        self.figure.axes.plot(lists[0],lists[1])
        self.figure.axes.figure.canvas.draw()
        self.figure.axes.figure.canvas.flush_events()
        print('end')
        print('begin')
        self.figure2.axes.cla()
        self.figure2.axes.plot(lists[2],lists[3])
        self.figure2.axes.figure.canvas.draw()
        self.figure2.axes.figure.canvas.flush_events()
        print('end')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    fileTest = FileTableWidget()
    fileTest.show()
    sys.exit(app.exec_())
