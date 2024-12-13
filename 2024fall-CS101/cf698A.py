n=int(input())
a=list(map(int, input().split()))
dp=[0]
aclast=0
for i in range(n):
    if a[i]==0:
        aclast=0
        dp.append(dp[-1]+1)
    elif a[i]==1:
        if aclast!=1:
            aclast=1
            dp.append(dp[-1])
        else:
            aclast=0
            dp.append(dp[-1]+1)
    elif a[i]==2:
        if aclast!=2:
            aclast=2
            dp.append(dp[-1])
        else:
            aclast=0
            dp.append(dp[-1]+1)
    else:
        if aclast==1:
            aclast=2
            dp.append(dp[-1])
        elif aclast==2:
            aclast=1
            dp.append(dp[-1])
        else:
            dp.append(dp[-1])
            aclast=-1
print(dp[-1])  
