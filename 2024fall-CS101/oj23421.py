n, b=map(int, input().split())
p=list(map(int, input().split()))
w=list(map(int, input().split()))
dp=[[0 for i in range(b+1)] for j in range(n)]
for i in range(n):
    for j in range(1, b+1):
        if j>=w[i]:
            dp[i][j]=max(dp[i-1][j], dp[i-1][j-w[i]]+p[i])
        else:
            dp[i][j]=dp[i-1][j]
print(dp[-1][-1])
