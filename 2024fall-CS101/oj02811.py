from copy import deepcopy
n=5
m=6
b=[]
def elim(list0, list1, i):
    s=list1[i]/list0[i]
    for k in range(n*m+1):
        list1[k]-=list0[k]*s
        list1[k]=round(list1[k])
        list1[k]%=2
        
for i in range(n):
    b+=list(map(int, input().split()))
    
mat=[[0 for i in range(m*n)] for j in range(m*n)]
for i in range(m*n):
    mat[i][i]=1
    if i%m!=0:
        mat[i][i-1]=1
    if i%m!=m-1:
        mat[i][i+1]=1
    if i//m!=0:
        mat[i][i-m]=1
    if i//m!=n-1:
        mat[i][i+m]=1
a=[]
for i in range(m*n):
    a.append([])
    a[i]=mat[i]+[b[i]]
#高斯消元
for i in range(n*m):
    #寻找主元
    for j in range(i, n*m):
        if a[j][i]!=0:
            a[i], a[j]=a[j], a[i]
            break
        
    #消元
    for j in range(i+1, n*m):
        elim(a[i], a[j], i)
#回代
for i in range(n*m-1, -1, -1):
    a[i][n*m]/=a[i][i]
    a[i][i]=1
    
    for j in range(0, i):
        a[j][n*m]-=a[j][i]*a[i][n*m]
        a[j][i]=0

#得到解
ans=[]
for i in range(n*m):
    ans.append(int(a[i][n*m])%2)
#输出
for i in range(n):
    print(*ans[m*i:m*(i+1)])
