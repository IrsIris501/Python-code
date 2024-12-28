def judge(mid):
    M=0
    before=stone[0]
    for i in range(1, n+2):
        if stone[i]-before<mid:
            M+=1
        else:
            before=stone[i]
    return M<=m
l, n, m=map(int, input().split())
stone=[0]
for i in range(n):
    stone.append(int(input()))
stone.append(l)
left=0
right=l+2
while left<right:
    mid=(left+right+1)//2
    if judge(mid):
        left=mid
    else:
        right=mid-1
print(left)
