from heapq import *
while True:
    try:
        n=int(input())
    except:
        break
    b=list(map(int, input().split()))
    k=2
    s=sum(b)
    b.sort()
    while True:
        if b[-1]>s/k:
            a=b.pop(-1)
            k-=1
            s-=a
        else:
            break
    print('%.1f' %(s/k))
