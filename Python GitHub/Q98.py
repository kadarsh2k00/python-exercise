s=input()
l=[]
for i in range(0,len(s)):
    if i%2==0:
        l.append(s[i])
print(''.join(l))
