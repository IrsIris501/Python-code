n, t=map(int, input().split())
p=list(map(int, input().split()))
v=sum(p)-t
if v<0:
    print(0)
elif v==0:
    print(t)
else:
    dp=[[i for i in range(v+1)] for j in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, v+1):
            if j>=p[i-1]:
                dp[i][j]=min(dp[i-1][j], dp[i-1][j-p[i-1]])
            else:
                dp[i][j]=dp[i-1][j]
    print(dp[-1][-1]+t)
