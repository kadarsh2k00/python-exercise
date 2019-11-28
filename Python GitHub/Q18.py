p=input().split(',')
l=[]
for x in p:
    c=0
    d=0
    e=0
    f=0
    if len(x)>5 and len(x)<13:
            for i in range (0,len(x)):
                if x[i].isdigit():
                    f=f+1
                if x[i].isupper():
                    d=d+1
                if x[i].islower():
                    e=e+1
                if x[i]=='@' or x[i]=='$' or x[i]=='#':
                    c=c+1
    if c!=0 and d!=0 and e!=0  and f!=0:
        l.append(x)
print(','.join(l))
        
    
