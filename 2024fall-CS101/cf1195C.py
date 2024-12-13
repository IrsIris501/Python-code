n=int(input())
r1=list(map(int, input().split()))
r2=list(map(int, input().split()))
dp0=[0]
dp1=[0]
dp2=[0]
for i in range(n):
    dp0.append(max(dp1[i], dp2[i]))
    dp1.append(max(dp0[i], dp2[i])+r1[i])
    dp2.append(max(dp0[i], dp1[i])+r2[i])
print(max(dp0[-1], dp1[-1], dp2[-1]))
