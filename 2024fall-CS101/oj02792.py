n=int(input())
for i in range(n):
    s=int(input())
    a=input()
    A=list(map(int, input().split()))
    b=input()
    B=list(map(int, input().split()))
    sa=set(A)
    sb=set(B)
    da={}
    db={}
    for i in sa:
        da[i]=A.count(i)
    for i in sb:
        db[i]=B.count(i)
    ans=0
    for i in da.keys():
        for j in db.keys():
            if i+j==s:
                ans+=da[i]*db[j]
                break
    print(ans)
    
