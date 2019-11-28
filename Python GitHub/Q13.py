s=input().split(' ')
c=0
d=0
for i in range (0,len(s)):
    for k in s[i]:
        if k.isdigit():
            c=c+1
        elif k.isalpha():
            d=d+1
print('LETTERS:',d)
print('DIGITS:',c)
