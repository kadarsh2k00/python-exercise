class Person:
    def __init__(self):
        pass
    def getgender(self):
        pass
class Male(Person):
    def getgender(self):
        return 'Male'
class Female(Person):
    def getgender(self):
        return 'Female'

p1=Male()
p2=Female()
print(p1.getgender())
print(p2.getgender())
