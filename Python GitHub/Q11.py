s=input().split(',')
l=[]
for x in s:
    if int(x,2)%5==0:
        l.append(x)
print(','.join(l))
