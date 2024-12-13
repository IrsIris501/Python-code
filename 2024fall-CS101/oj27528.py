n=int(input())
dp=[0 for i in range(n+1)]
dp[0]=1
dp[1]=1
for i in range(2, n+1):
    tmp=0
    for j in range(1, i):
        tmp+=dp[j]
    dp[i]=tmp+1
    
print(dp[n])

