n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
m=max(a)
f=[1, 1]
for i in range(2, m):
    f.append(f[i-1]+f[i-2])
for i in range(n):
    print(f[a[i]-1])
