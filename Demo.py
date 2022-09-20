import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import ttk
import datetime as dt
from math import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
import threading
from matplotlib.animation import FuncAnimation


def call():
    t1 = threading.Thread(target=update)
    t1.start()


def update(duration=100, interval=0.1):
    fig = plt.figure(1, (10, 7.5), dpi=100)
    ax1 = fig.add_subplot(511)
    ax2 = fig.add_subplot(512)
    ax3 = fig.add_subplot(513)
    ax4 = fig.add_subplot(514)
    ax5 = fig.add_subplot(515)
    fig.set_tight_layout(tight=TRUE)
    l = []
    m = []
    n = []
    x = []
    # for i in range(duration):
    i = 0
    while duration:
        plt.pause(interval)
        l.append(scale1.get())
        m.append(sin(scale1.get()))
        n.append(cos(scale1.get()))
        x.append(i)
        ax1.set_title(label="var1")
        ax1.plot(range(len(l)), l, '-r', label='temperature')
        ax1.set_xticks(x)
        ax1.set_xticklabels(l)

        # plt.xticks(range(len(n)), n)
        ax2.set_title(label="var2")
        ax2.plot(x, n, '-c')
        ax3.set_title(label="var3")
        ax3.plot(x, m, '-m')
        ax4.set_title(label="var4")
        ax4.plot(x, n, '-y')
        ax5.set_title(label="var5")
        ax5.plot(x, m, '-b')
        i += 1
    # plt.draw()


def display():
    plt.clf()
    fig = plt.figure(1, (10, 7.5), dpi=100)
    # ax1 = fig.add_subplot(511)
    # ax2 = fig.add_subplot(512)
    # ax3 = fig.add_subplot(513)
    # ax4 = fig.add_subplot(514)
    # ax5 = fig.add_subplot(515)

    canvas = FigureCanvasTkAgg(fig, master=frm1)  # A tk.DrawingArea.
    canvas.draw()
    # 显示画布
    canvas.get_tk_widget().pack()
    # 创建工具条
    toolbar = NavigationToolbar2Tk(canvas, frm1)
    toolbar.update()
    # 显示工具条
    canvas.get_tk_widget().pack()


win = Tk()
win.geometry('600x600')
win.resizable(width=False, height=False)
win.title('PLC-Trend')
frm1 = Frame(win, height=500, width=500)
frm1.place(x=0, y=0)

lab1 = Label(win, text="IP地址:")
lab1.place(x=10, y=10)
en1 = Entry(win)
en1.place(x=60, y=10)

lab2 = Label(win, text="OPC-UAServer地址:")
lab2.place(x=10, y=40)
en2 = Entry(win, width=30)
en2.place(x=120, y=40)

lab3 = Label(win, text="根节点:")
lab3.place(x=10, y=70)
cv = StringVar()
com = ttk.Combobox(win, textvariable=cv)
com.place(x=120, y=70)
# 设置下拉数据
com["value"] = ("0", "1", "2")
# 设置默认值
com.current(0)


# 绑定事件
def func(event):
    print(com.get())
    print(cv.get())


com.bind("<<ComboboxSelected>>", func)

scale1 = Scale(win, from_=0, to=100, orient=VERTICAL, tickinterval=10, length=200)
scale1.pack()

but1 = Button(win, width=10, text="开始记录", command=call)
but1.place(x=500, y=10)

win.mainloop()
