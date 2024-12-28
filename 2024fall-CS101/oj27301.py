n, a, b=map(int, input().split())
da=a
db=b
f=list(map(int, input().split()))
w=[0 for i in range(n)]
pointer=0
ans=0
if n%2==0:
    while pointer!=n//2:
        if da<f[pointer]:
            da=a
            ans+=1
        if db<f[n-1-pointer]:
            db=b
            ans+=1
        da-=f[pointer]
        db-=f[n-1-pointer]
        pointer+=1
else:
    while pointer!=n//2:
        if da<f[pointer]:
            da=a
            ans+=1
        if db<f[n-1-pointer]:
            db=b
            ans+=1
        da-=f[pointer]
        db-=f[n-1-pointer]
        pointer+=1
    if max(da, db)<f[pointer]:
        ans+=1
print(ans)
    
