t=int(input())
for _ in range(t):
    n=int(input())
    ans=n*(n+1)//2
    bn=bin(n)
    p=len(str(bn))-2
    ans-=(2**(p+1)-2)
    print(ans)
