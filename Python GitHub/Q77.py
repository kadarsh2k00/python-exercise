import random
p=random.choice([ x for x in range(0,10) if x%5==0 and x%7==0])
print(p)
