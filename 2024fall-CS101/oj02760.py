n=int(input())
tri=[]
for i in range(n):
    tri.append(list(map(int, input().split())))
ans=[tri[0]]
for i in range(1, n):
    temp=[]
    for j in range(i+1):
        if j==0:
            temp.append(ans[i-1][0]+tri[i][0])
        elif j==i:
            temp.append(ans[i-1][-1]+tri[i][-1])
        else:
            temp.append(max(ans[i-1][j-1], ans[i-1][j])+tri[i][j])
    ans.append(temp)
print(max(ans[-1]))
