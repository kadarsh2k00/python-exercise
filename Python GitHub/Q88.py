l=[12,24,35,70,88,120,155]
##for i in range(len(l)-1,-1,-1):
##    if l[i]%5==0 and l[i]%7==0:
##        del(l[i])
l=[x for x in l if x%35!=0]
print(l)
    
