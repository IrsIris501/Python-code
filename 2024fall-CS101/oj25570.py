n=int(input())
mat=[]
k=n
tmp=0
for i in range(n):
    mat.append(list(map(int, input().split())))
matt=[[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        matt[i][j]=mat[j][i]
while k>0:
    start=(n-k)//2
    end=(n+k)//2
    
    s=sum(mat[start][start:end])+sum(mat[end-1][start:end])+sum(matt[start][start:end])+sum(matt[end-1][start:end])
    s-=(mat[start][start]+mat[start][end-1]+mat[end-1][start]+mat[end-1][end-1])
    if s>tmp:
        tmp=s
    k-=2
if n%2==1:
    if mat[n//2][n//2]>tmp:
        tmp=mat[n//2][n//2]
print(tmp)

    
