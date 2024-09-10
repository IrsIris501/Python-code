import math
n=int(input())
a=[]
limit=int(math.sqrt(n))
for i in range(2, limit+1):
    while n%i==0:
        a.append(i)
        n/=i
if n!=1:
    a.append(n)
flag=0
for i in range(len(a)-1):
    if a[i]==a[i+1]:
        flag=1
        break
if flag==1:
    print(0)
elif len(a)%2==0:
    print(1)
else:
    print(-1)
