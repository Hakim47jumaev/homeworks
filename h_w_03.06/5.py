class Rectangle:
    def __init__(self,len) :
        self.len=len
    def is_valid_len(self):
        if self.len>0:
            return True
        else:
            return False

re1=Rectangle(30)
print(re1.is_valid_len())
        