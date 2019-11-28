def fun(n):
    if n==0:
        return 0
    else:
        return fun(n-1)+100
s=int(input())
print(fun(s))
