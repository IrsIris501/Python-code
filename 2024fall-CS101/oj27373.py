m=int(input())
n=int(input())
a=input().split()
for i in range(n):
    for j in range(n-1-i):
        if a[j]+a[j+1]<a[j+1]+a[j]:
            a[j],a[j+1]=a[j+1],a[j]
dp=[["" for i in range(n)] for j in range(m+1)]
for j in range(n):
    for i in range(1, m+1):
        if len(a[j])<=i and len(dp[i-len(a[j])][j-1]+a[j])==i:
            dp[i][j]=max(dp[i-len(a[j])][j-1]+a[j], dp[i][j-1])
        else:
            dp[i][j]=dp[i][j-1]
for i in range(m, -1, -1):
    if dp[i][-1]!="":
        print(dp[i][-1])
        break
