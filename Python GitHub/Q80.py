import random
p=random.sample([x for x in range(1,1000) if x%5==0 and  x%7==0],5)
print(p)
##l=[]
##for i in range(1,1000):
##    if i%5==0 and i%7==0:
##        l.append(i)
##print(random.sample(l,5))
