a=list(map(int, input().split(',')))
n=len(a)
dp1=[]
dp2=[]
dp1.append(a[0])
dp2.append(a[0])

for i in range(1, n):
    dp1.append(max(dp1[i-1]+a[i], a[i]))
    dp2.append(max(dp1[i-1], a[i], dp2[i-1]+a[i]))
print(max(dp2))
