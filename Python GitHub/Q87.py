l=[5,6,77,45,22,12,24]
for i in range(len(l)-1,-1,-1):
    if l[i]%2==0:
        del(l[i])

##l=[i for i in l if i%2!=0]
print(l)
