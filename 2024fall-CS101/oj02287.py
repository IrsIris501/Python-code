while True:
    n=int(input())
    if not n:
        break
    th=list(map(int, input().split()))
    kh=list(map(int, input().split()))
    th.sort()
    kh.sort()
    ans=0
    while th!=[]:
        if th[-1]>kh[-1]:
            th.pop(-1)
            kh.pop(-1)
            ans+=200
        elif th[-1]<kh[-1]:
            th.pop(0)
            kh.pop(-1)
            ans-=200

        else:
            if th[0]>kh[0]:
                th.pop(0)
                kh.pop(0)
                ans+=200
            else:
                if th[0]<kh[-1]:
                    ans-=200
                th.pop(0)
                kh.pop(-1)
                
    print(ans)
