class Calculator:

    num = 100

    def __init__(self, a, b):
        print("default Constructor is called")
        self.a = a
        self.b = b

    def getdata(self):
        print("Getdata is called succussfully")

    def summation(self):
        c = self.a + self.b + self.num
        return c


obj = Calculator(2, 3)
obj.getdata()
print(obj.summation())