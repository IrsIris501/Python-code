n=int(input())
for i in range(n):
    s=list(map(float, input().split()))
    a=s[0]
    b=s[1]
    c=s[2]
    delta=b*b-4*a*c
    head=-b/(2*a)
    if delta>0:
        x1=head+(delta**0.5)/(2*a)
        x2=head-(delta**0.5)/(2*a)
        print("x1=%(x1).5f;x2=%(x2).5f"%{'x1':x1, 'x2':x2})
    elif delta==0:
        print("x1=x2=%.5f"%head)
    else:
        delta=-delta
        d=(delta**0.5)/(2*a)
        print('x1=%(xre).5f+%(d).5fi;x2=%(xre).5f-%(d).5fi'%{'xre':head, 'd':d})
        
