n, m=input().split()
n=int(n)
m=int(m)
t=[]
for i in range(n+1):
    t.append(1)
for i in range(m):
    a, b=input().split()
    a=int(a)
    b=int(b)
    for j in range(a, b+1):
        t[j]=0
ans=0
for i in range(n+1):
    if t[i]==1:
        ans+=1
print(ans)
