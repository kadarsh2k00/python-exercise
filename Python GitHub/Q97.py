s=input()
p=[]
for i in range(len(s)-1,-1,-1):
    p.append(s[i])
print(''.join(p))
