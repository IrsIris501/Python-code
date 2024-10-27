n=int(input())
a=list(map(int, input().split()))
s=sum(a)
if s%3!=0:
    print(0)
else:
    slist=[]
    rslist=[]
    temp=0
    ans=0
    for i in range(n-1):
        temp+=a[i]
        if temp==s//3:
            slist.append(1)
        else:
            slist.append(0)
        
        
    temp=0
    slist.pop()
    for i in range(n-1, 1, -1):
        temp+=a[i]
        if temp==s//3:
            rslist.append(1)
        else:
            rslist.append(0)
    r=[]
    temp=0
    
    for i in range(n-2):
        temp+=rslist[i]
        r.append(temp)
    for i in range(n-2):
        ans+=r[i]*slist[n-3-i]
    
    print(ans)



    
            
