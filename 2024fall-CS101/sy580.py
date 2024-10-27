n, m=input().split()
n=int(n)
m=int(m)
matrix=[]
for i in range(n):
    matrix.append(list(map(int, input().split())))
ans=0
for i in range(n):
    for j in range(m):
        a=matrix[i][j]*(1000*matrix[0][j]+100*matrix[i][-1]+10*matrix[-1][j]+matrix[i][0])
        if a>ans:
            ans=a
print(ans)
