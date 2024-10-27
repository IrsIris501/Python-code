def surround(a:list, i:int, j:int):
    temp=0
    for k in range(i-1, i+2):
        temp+=sum(a[k][j-1:j+2])
    if a[i][j]:
        if temp<3:
            return 0
        elif temp>4:
            return 0
        else:
            return 1
    else:
        if temp==3:
            return 1
        else:
            return 0

n, m=input().split()
n=int(n)
m=int(m)
a=[[0]*m]
for i in range(n):
    a.append([0])
    l=list(map(int, input().split()))
    a[i+1]+=l
    a[i+1]+=[0]
a.append([0]*m)
ans=[]
for i in range(n):
    ans.append([])
    for j in range(m):
        ans[i].append(surround(a, i+1, j+1))
for i in range(n):
    print(*ans[i])
