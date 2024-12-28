import math
t=int(input())
s=''
for i in range(1, 100):
    for j in range(1, i+1):
        s+=str(j)
for k in range(t):
    n=int(input())
    if n<=9045:
        print(s[n-1])
    else:
        start=math.floor(math.sqrt(n))
        
        
