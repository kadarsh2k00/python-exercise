l=[1,2,3,4,5,6,7,8,9,10]

def even(n):
    if n%2==0:
        return True
    
x=(filter(even,l))
for i in x:
    print(i)

