m=int(1e9)+7

t, k=map(int, input().split())
dp=[0 for i in range(100001)]
dp[0]=1
for i in range(1, 100001):
    if i-k>=0:
        dp[i]=(dp[i-1]+dp[i-k])%m
    else:
        dp[i]=dp[i-1]
ds=[0 for i in range(100001)]
ds[0]=1
for i in range(1, 100001):
    ds[i]=ds[i-1]+dp[i]
for i in range(t):
    a, b=map(int, input().split())
    print((ds[b]-ds[a-1])%m)
