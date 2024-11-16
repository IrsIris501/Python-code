def sgn(x):
    if x>0:
        return 1
    elif x==0:
        return 0
    else:
        return -1
n=int(input())
a=list(map(int, input().split()))
d=[[1, 0]]
for i in range(1, n):
    temp=[[1, 0]]
    
    for j in range(i):
        if a[i]!=a[j] and (a[i]-a[j])*d[j][1]<=0:
            temp.append([d[j][0]+1, sgn(a[i]-a[j])])
    temp.sort(reverse=True)
    flag=temp[0][1]
    for i in range(1, len(temp)):
        if temp[i][0]!=temp[i-1][0]:
            break
        if temp[i][1]!=flag:
            flag=0
            break
    d.append([temp[0][0], flag])

print(d[-1][0])
