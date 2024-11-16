n, a, b, c=map(int, input().split())
s=[a, b, c]
ans=[0]
for i in range(1, n+1):
    temp=[]
    for j in s:
        if i>=j and ans[i-j]!=-1:
            temp.append(ans[i-j]+1)
    if temp!=[]:
        ans.append(max(temp))
    else:
        ans.append(-1)
print(ans[-1])
