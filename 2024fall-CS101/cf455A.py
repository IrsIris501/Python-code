n=int(input())
a=[0]*100001
s=list(map(int, input().split()))
for i in s:
    a[i]+=1
dp=[0, a[1]]
for i in range(2, 100001):
    dp.append(max(dp[i-1], dp[i-2]+a[i]*i))
print(dp[100000])
