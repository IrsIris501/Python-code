t, m=map(int, input().split())
p=[]
c=[]
def func(c, p, t, m):
    dp=[0 for i in range(t+1)]
    for i in range(1, t+1):
        for j in range(m):
            if i>=c[j]:
                dp[i]=max(dp[i], dp[i-c[j]]+p[j])
    return dp[-1]
for i in range(m):
    a, b=map(int, input().split())
    c.append(a)
    p.append(b)

print(func(c, p, t, m))
