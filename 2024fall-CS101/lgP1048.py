t, m=map(int, input().split())
c=[]
p=[]
for i in range(m):
    a, b=map(int, input().split())
    c.append(a)
    p.append(b)
dp=[[0 for i in range(t+1)] for j in range(m)]
for i in range(m):
    for j in range(1, t+1):
        if j>=c[i]:
            dp[i][j]=max(dp[i-1][j], dp[i-1][j-c[i]]+p[i])
        else:
            dp[i][j]=dp[i-1][j]
print(dp[-1][-1])
