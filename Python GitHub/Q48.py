
##def even(n):
##    if n%2==0:
##        return True
##l=[]
##for i in range(1,21):
##    l.append(i)
##x=filter(even,l)
x=(filter(lambda x:x%2==0,range(1,21)))
for i in x:
    print(i)
    

