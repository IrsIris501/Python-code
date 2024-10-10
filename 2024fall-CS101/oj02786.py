n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
m=max(a)
f=[1, 2]
for i in range(2, m):
    f.append((2*f[i-1]+f[i-2])%32767)
for i in range(n):
    print(f[a[i]-1])
