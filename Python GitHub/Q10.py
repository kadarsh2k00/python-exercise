s=input().split(' ')
unique=[]
for  x in s:
    if x not in unique:
        unique.append(x)
p=sorted(unique)
print(' '.join(p))
