def binary(array,u,l,x):
    c=-1
    while l<=u and c==-1:
        mid=(l+u)//2
        if array[mid]==x:
            c=mid       
        elif array[mid]>x:
            u=mid-1
        elif array[mid]<x:
            l=mid+1
    return c
array=[2,5,7,9,11,17,222]
x=int(input())
l=0
u=(len(array)-1)
p=binary(array,u,l,x)
if p!=-1:
    print(x,'found at',p)
else:
    print(x,'Not found')

    
    
    
    
