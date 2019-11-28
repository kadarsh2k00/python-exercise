
X,Y=input().split(',')
X=int(X)
Y=int(Y)
A=[]
for i in range(0,X):
    B=[]
    for j in range(0,Y):
        B.append(int(j*i))
    A.append(B)
print(A)
