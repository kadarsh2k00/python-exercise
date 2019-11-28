s=input().split(' ')
c=0
d=0
for i in range (0,len(s)):
    for k in s[i]:
        if k.isupper():
            c=c+1
        elif k.islower():
            d=d+1
print('LOWER CASE:',d)
print('UPPER CASE:',c)

