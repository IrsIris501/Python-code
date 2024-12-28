m=int(input())
for i in range(m):
    l, n=input().split()
    l=int(l)
    n=int(n)
    x=list(map(int, input().split()))
    x.sort()
    time1=0
    for i in range(n):
        if x[i]>l/2 and l-x[i]>time1:
            time1=l-x[i]
        elif x[i]<=l/2 and x[i]>time1:
            time1=x[i]
    print(time1, end=' ')
    
    
    
