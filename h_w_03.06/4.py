class Rectangle:
    def __init__(self,length) :
        self.__length=length
    @property
    def leng(self):
        return self.__length
    @leng.setter
    def lenge(self,length):
        self.length=length
        print(self.length)

rec1=Rectangle
rec1.lenge()
