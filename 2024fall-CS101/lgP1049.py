v=int(input())
n=int(input())
item=[]
for i in range(n):
    item.append(int(input()))
dp=[[i for i in range(v+1)] for j in range(n+1)]
for i in range(1, n+1):
    for j in range(1, v+1):
        if j>=item[i-1]:
            dp[i][j]=min(dp[i-1][j], dp[i-1][j-item[i-1]])
        else:
            dp[i][j]=dp[i-1][j]
print(dp[-1][-1])
