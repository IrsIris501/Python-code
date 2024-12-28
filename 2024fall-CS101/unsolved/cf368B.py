n, m=map(int, input().split())
a=list(map(int, input().split()))
ans=[0]*(n+1)
dp=[]
for i in range(n-1, -1, -1):
    if a[i] not in dp:
        dp.append(a[i])
        ans[i]=ans[i+1]+1
    else:
        ans[i]=ans[i+1]
for i in range(m):
    l=int(input())
    print(ans[l-1])
