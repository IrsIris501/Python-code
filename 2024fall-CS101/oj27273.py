t=int(input())
for i in range(t):
    a=int(input())
    b=a
    m=0
    while a>=2:
        a/=2
        m+=1
    ans=b*(b+1)/2
    ans-=2*(2**(m+1)-1)
    print(int(ans))
