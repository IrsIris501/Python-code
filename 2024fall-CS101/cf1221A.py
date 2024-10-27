import math
t=int(input())
for i in range(t):
    n=int(input())
    s=list(map(int, input().split()))
    s.sort()
    a=[0 for _ in range(12)]
    for j in range(n):
        if s[j]>2048:
            break
        a[int(math.log2(s[j]))]+=1
    ans=0
    for j in range(12):
        ans+=a[j]
        if j!=11:
            ans=ans//2
    if ans>=1:
        print("YES")
    else:
        print("NO")
