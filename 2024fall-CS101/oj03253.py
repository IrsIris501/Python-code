while True:
    l=list(map(int, input().split()))
    if l==[0, 0, 0]:
        break
    n=l[0]
    p=l[1]
    m=l[2]
    a=[]
    for i in range(n):
        a.append(i+1)
    j=p-1
    while len(a)>1:
        j+=m
        if j>len(a):
            j%=len(a)
        print(a.pop(j-1), end=',')
        if j>0:
            j-=1
    print(a[0])
    
