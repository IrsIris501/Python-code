def fp(n):
    if n==1:
        a=["1"]
        return a
    temp=fp(n-1)
    a=[]
    for i in range(n):
        for j in range(len(temp)):
            a.append(temp[j][0:i:1]+str(n)+temp[j][i::])
    return a

n=int(input())
ans=fp(n)
ans.sort()
map(list, ans)
for i in range(len(ans)):
    print(*ans[i])
