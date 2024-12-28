def minus520(x):
    return int(x)-520
def func(g, n):
    for i in range(n, 0, -1):
        tmp=0
        for j in range(0, n-i+1):
            if j==0:
                tmp=sum(g[0:i])
            else:
                tmp+=(g[j+i-1]-g[j-1])
            if tmp==0:
                return i
    return 0
n=int(input())
g=list(map(minus520, input().split()))
print(func(g, n)*520)
