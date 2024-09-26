
m=int(input())
for i in range(m):
    ans=0
    n=int(input())
    jail=[]
    for j in range(n):
        jail.append(0)
    for j in range(1, n+1):
        k=j
        
        while k<=n:
            if jail[k-1]==0:
                jail[k-1]=1
            else:
                jail[k-1]=0
            k+=j
    for j in range(n):
        if jail[j]==1:
            ans+=1
    print(ans)
        
