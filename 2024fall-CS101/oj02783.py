while True:
    n=int(input())
    if n==0:
        break
    a=[]
    for i in range(n):
        l=list(map(int, input().split()))
        a.append((l[1],l[0]))
    cd=sorted(a)
    ans=1
    distmax=cd[0][1]
    for i in range(n):
        if cd[i][1]<distmax:
            distmax=cd[i][1]
            ans+=1
    print(ans)

