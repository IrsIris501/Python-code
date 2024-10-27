while True:
    r, n=input().split()
    r=int(r)
    n=int(n)
    if r==n==-1:
        break
    a=list(map(int, input().split()))
    a.append(10001)
    a.append(-10001)
    a.append(-10001)
    a.sort()
    ans=0
    farthest=10001
    while len(a)>2:
        while farthest-a[-1]<=r:
            a.pop(-1)
        if len(a)<=2:
            break
        if a[-1]-a[-2]<=r:
            while a[-1]-a[-3]<=r:
                a.pop(-2)
            farthest=a[-2]
            ans+=1
            a.pop(-1)
            a.pop(-1)
        else:
            farthest=a[-1]
            a.pop(-1)
            ans+=1
    print(ans)
