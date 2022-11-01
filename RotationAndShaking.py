class GetTxtData:

    def __init__(self):
        self.rotation_path = 'C:/Users/RY/Desktop/my/识别2.txt'
        self.shaking_path = 'C:/Users/RY/Desktop/my/识别1.txt'

    def getRotationData(self):
        with open(self.rotation_path, "r") as file:
            asd = file.readline()
        num = self.changeType(asd)
        return num

    def getShakingData(self):
        with open(self.shaking_path, "r") as file:
            asd = file.readline()
        num = self.changeType(asd)
        return num

    @staticmethod
    def changeType(num):
        try:
            num1 = num.strip()
            num2 = float(num1)
            return num2
        except Exception:
            return 0


if __name__ == '__main__':
    data = GetTxtData()
    while True:
        res1 = data.getRotationData()
        res2 = data.getShakingData()
