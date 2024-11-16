n, m=map(int, input().split())
c=list(map(int, input().split()))
c.sort()
num=[0]
for i in range(1, m+1):
    temp=[]
    for j in c:
        if i>=j:
            if num[i-j]!=-1:
                temp.append(num[i-j]+1)
        else:
            break
    if temp!=[]:
        num.append(min(temp))
    else:
        num.append(-1)
print(num[-1])
