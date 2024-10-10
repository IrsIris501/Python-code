t=0
while True:
    t+=1
    l=list(map(int, input().split()))
    if l==[-1, -1, -1, -1]:
        break
    p=l[0]%23
    e=l[1]%28
    i=l[2]%33
    d=l[3]+1
    if d%33>i:
        d=(d//33+1)*33+i
    else:
        d=(d//33)*33+i
    while d%23!=p or d%28!=e:
        d+=33
    ans=d-l[3]
    print("Case {case}: the next triple peak occurs in {a} days.".format(case=t, a=ans))
    
