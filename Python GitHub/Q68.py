def even(n):
    for i in range(1,n+1):
        if i%2==0:
           yield i
m=int(input())
x=even(m)
p=list(x)
for i in range(len(p)):
    p[i]=str(p[i])
    
print(','.join(p))
