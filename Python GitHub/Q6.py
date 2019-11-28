import math
n=(input().split(','),int)
c=50
h=30
p=[]
for i in range(0,len(n[0])):
    s=(2*c*int(n[0][i]))//h
    Q=math.sqrt(s)
    p.append(str(int(Q)))
print(','.join(p))
