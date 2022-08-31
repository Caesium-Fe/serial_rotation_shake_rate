import serial
import matplotlib.pyplot as plt
import numpy as np
import time


def init_serial():
    ser = serial.Serial()
    return ser


# def open_true_fail(ser):
#     if ser.isOpen():
#         print(ser.name + "open success!")
#     else:
#         print(ser.name + "open fail!")


# 创建画布
plt.grid(True) # 添加网格
plt.ion()
plt.figure(1)
plt.xlabel('rotation')
plt.ylabel('shake')
plt.title('rotation_shake_rate')

# 设置串口
ser1 = init_serial()
ser2 = init_serial()
ser1.port = ''
ser2.port = ''
ser1.baudrate = 0
ser2.baudrate = 0
ser1.bytesize = 8
ser2.bytesize = 8
ser1.parity = serial.PARITY_NONE
ser2.parity = serial.PARITY_NONE
ser1.stopbits = 1
ser2.stopbits = 1
ser1.timeout = 0.001
ser2.timeout = 0.001

ser1.close()
ser2.close()

# # 判断接口是否正确连接
# open_true_fail(ser1)
# open_true_fail(ser2)

# 接收数据
rotation = []
shake = []
temperature = []

# 循环接收串口值
while True:

    if not ser1.isOpen:
        ser1.open()
    if not ser2.isOpen:
        ser2.open()
    time.sleep(0.05)
    num1 = ser1.inWaiting()
    num2 = ser2.inWaiting()
    if num1 and num2:
        # 解析出来是字符串
        data1 = ser1.read(num1).decode('UTF-8')
        # 解析出来是二进制
        data2 = ser2.read(1)
        intdata = int.from_bytes(data2,byteorder='big',signed=False)
        rotation.append(data1)
        shake.append(intdata)
        plt.plot(rotation,shake,'-r')
        plt.draw()
    time.sleep(0.002)