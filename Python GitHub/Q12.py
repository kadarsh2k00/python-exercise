l=[]
for i in range (1000,3001):
    n=i
    c=0
    while(n!=0):
        r=n%10
        n=n//10
        if r%2==0:
            c=c+1
    if c==4:
        l.append(i)
for i in range (0,len(l)):
    l[i]=str(l[i])
print(','.join(l))
