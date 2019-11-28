class Customerror(Exception):
##    pass
##raise Customerror("Custom error created succesfully")

   def __init__(self,string):
        self.msg=string

s=Customerror('Error Occured')
print(s.msg)
