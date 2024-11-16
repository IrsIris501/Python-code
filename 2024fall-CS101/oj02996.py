def thenext(x):
    flag=1
    for i in range(len(x)-1, 0, -1):
        if x[i-1]<x[i]:
            flag=0
            y=x[i-1:len(x):1]
            mmin=len(x)+1
            for j in range(1, len(y)):
                if y[j]>y[0] and y[j]<mmin:
                    mmin=y[j]
            y.remove(mmin)
            y.sort()
            ans=x[0:i-1]+[mmin]+y
            break
    if flag:
        ans=sorted(x)
    return ans

n=int(input())
m=int(input())
a=list(map(int, input().split()))
for i in range(m):
    b=thenext(a)
    a=b
print(*a)
