s=input().split(',')
l=[]
for i in range(0,len(s)):
    s[i]=int(s[i])
    if s[i]%2!=0:
        s[i]=s[i]**2
        s[i]=str(s[i])
        l.append(s[i])
print(','.join(l))
