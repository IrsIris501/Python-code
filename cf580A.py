n=int(input())
a=list(map(int, input().split()))
a.append(-114514)
b=[]
c=1
for i in range(1, n+1):
    if a[i]>=a[i-1]:
        c+=1
    else:
        b.append(c)
        c=1
print(max(b))
