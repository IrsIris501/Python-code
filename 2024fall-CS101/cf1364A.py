import math
t=int(input())
for i in range(t):
    n, x=input().split()
    n=int(n)
    x=int(x)
    l=list(map(int, input().split()))
    for i in range(n):
        l[i]=l[i]%x
    if sum(l)%x!=0:
        print(n)
    else:
        flag=1
        for i in range(min(math.ceil(n/2)+1, n)):
            if l[i]!=0 or l[n-1-i]!=0:
                print(n-1-i)
                flag=0
                break
        if flag:
            print(-1)
