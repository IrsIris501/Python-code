n=int(input())
a=list(map(int, input().split()))
e=[1]
for i in range(1, n):
    temp=[]
    for j in range(i):
        if a[j]<a[i]:
            temp.append(e[j]+1)
    if temp!=[]:
        e.append(max(temp))
    else:
        e.append(1)
print(max(e))
