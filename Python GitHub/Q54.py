class shape:
    def area(self):
        return (0)
    
class square(shape):
    def __init__(self,l):
        self.l=l
    def area(self):
        self.area=(self.l**2)
        return (self.area)
        
s1=square(5)
s2=shape()
print(s1.area())
print(s2.area())
    
    
