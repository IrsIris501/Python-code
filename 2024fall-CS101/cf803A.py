n, k=map(int, input().split())
a=[]
if n*n<k:
    print(-1)
else:
    for i in range(n):
        a.append([])
        for j in range(n):
            a[i].append(0)
    flag=1
    if k!=0:   
        for i in range(n):
            for j in range(n-i):
                if not j:
                    a[i][i]=1
                    k-=1
                    if k==0:
                        flag=0
                        break
                elif k==1:
                    a[i+1][i+1]=1
                    flag=0
                    break
                else:
                    a[i][i+j]=1
                    a[i+j][i]=1
                    k-=2
                    if k==0:
                        flag=0
                        break
            if not flag:
                break
    for i in range(n):
        print(*a[i])
            

