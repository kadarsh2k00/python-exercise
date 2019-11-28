t=(1,2,3,4,5,6,7,8,9,10)
l=[]
for x in t:
    if x%2==0:
        l.append(x)
print(tuple(l))
