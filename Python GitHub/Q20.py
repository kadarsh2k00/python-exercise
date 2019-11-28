class Div:
    def __init__(self):
        self.n=int(input())
    def genrator(self):
        for i in range(0,self.n):
            if i%7==0:
                print(i)

s=Div()
s.genrator()
