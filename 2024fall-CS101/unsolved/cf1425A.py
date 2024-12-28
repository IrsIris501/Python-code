n=int(input())
for i in range(n):
    m=int(input())
    i=0
    ans=0
    while m!=0:
        if m%2==0:
            m=m//2
            if i%2==0:
                ans+=m
        else:
            m-=1
            if i%2==0:
                ans+=1
        i+=1
    print(ans)
