l=[1,2,3,4,5,6,7,8,9,10]
s=[]

def square(n):
    return (n**2)
def even(n):
    if n%2==0:
        return True
    
x=map(square,l)
for i in x:
    s.append(i)

x1=filter(even,s)

for k in x1:
    print(k)
