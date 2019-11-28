import random
l=[]
for i in range(0,5):
    p=random.choice([x for x in range(100,200) if x%2==0])
    l.append(p)
    
print(l)
    
