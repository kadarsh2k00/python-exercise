print (abs.__doc__)
print (int.__doc__)
print (input.__doc__)

def fact(num):
    '''Return the factorial value of the input number.'''
    f=1
    for i in range(1,num+1):
        f=f*i
    return f

print (fact(5))
print (fact.__doc__)


