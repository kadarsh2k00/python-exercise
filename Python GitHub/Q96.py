s=input()
u=[]
for i in s:
    if i not in u:
        u.append(i)
for i in u:
    print(i,',',s.count(i))
    
