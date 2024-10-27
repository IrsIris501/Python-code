paras=list(map(int, input().split()))
m=paras[0]
n=paras[1]
p=paras[2]
q=paras[3]
mat=[]
core=[]
ans=[]
for i in range(m):
    mat.append(list(map(int, input().split())))
for i in range(p):
    core.append(list(map(int, input().split())))
for i in range(m-p+1):
    ans.append([])
    for j in range(n-q+1):
        elem=0
        for k in range(p):
            for l in range(q):
                elem+=mat[k+i][l+j]*core[k][l]
        ans[i].append(elem)
for i in range(m-p+1):
    print(*ans[i])
