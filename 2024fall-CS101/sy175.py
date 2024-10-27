n, k=input().split()
n=int(n)
k=int(k)
a=list(map(int, input().split()))
ans=0
last=n-1
for i in range(n):
    if i>=last:
        break
    for j in range(last, i, -1):
        if a[i]+a[j]==k:
            ans+=1
            last=j
            break
print(ans)
