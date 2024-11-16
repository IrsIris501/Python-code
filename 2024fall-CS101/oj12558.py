def isfringe(a, x, y):
    if a[x][y]==1:
        return 0
    temp=[a[i-1][j], a[i+1][j], a[i][j-1], a[i][j+1]]
    
    return temp.count(1)
n, m=map(int, input().split())
a=[[0]*(m+4), [0]*(m+4)]
for i in range(n):
    a.append([0, 0])
    a[i+2]+=list(map(int, input().split()))
    a[i+2]+=[0, 0]
a.append([0]*(m+4))
a.append([0]*(m+4))

cnt=0
for i in range(1, n+3):
    for j in range(1, m+3):
        cnt+=isfringe(a, i, j)
print(cnt)
