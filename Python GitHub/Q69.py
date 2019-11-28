def generator(n):
    for i in range(0,n):
        if i%5==0 and i%7==0:
            yield i
n=int(input())
x=generator(n)
p=list(x)
for i in range(len(p)):
    p[i]=str(p[i])
print(','.join(p))
