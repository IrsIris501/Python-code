def nextstep(pos, mode):
    a=mode%4
    if a==0:
        return [pos[0], pos[1]+1]
    elif a==1:
        return [pos[0]+1, pos[1]]
    elif a==2:
        return [pos[0], pos[1]-1]
    else:
        return [pos[0]-1, pos[1]]

n=int(input())
a=[]
for i in range(n):
    a.append([])
    for j in range(n):
        a[i].append(0)
i=1
pos=[0, -1]
mode=0
while i<=n*n:
    nsp=nextstep(pos, mode)
    if 0<=nsp[0]<=n-1 and 0<=nsp[1]<=n-1 and a[nsp[0]][nsp[1]]==0:
        a[nsp[0]][nsp[1]]=i
        i+=1
        pos=nsp
    else:
        mode+=1
for i in range(n):
    print(*a[i])
