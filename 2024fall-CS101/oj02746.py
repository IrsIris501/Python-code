while True:
    n, m=input().split()
    n=int(n)
    m=int(m)
    if n==m==0:
        break
    a=[]
    for i in range(n):
        a.append(i+1)
    j=0
    while len(a)>1:
        j+=m
        if j>len(a):
            j%=len(a)
        a.pop(j-1)
        if j>0:
            j-=1
    print(a[0])
    
