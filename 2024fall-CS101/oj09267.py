n, m=map(int, input().split())
dp=[[0, 0] for i in range(n+1)]
dp[0][0]=1
for i in range(1, n+1):
    if i<m:
        dp[i][0]=dp[i-1][0]+dp[i-1][1]
        dp[i][1]=dp[i-1][0]+dp[i-1][1]
    else:
        dp[i][0]=dp[i-1][0]+dp[i-1][1]
        dp[i][1]=dp[i-1][0]+dp[i-1][1]-dp[i-m][0]
print(dp[n][0]+dp[n][1])
