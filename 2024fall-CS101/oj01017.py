n=''
while n!='0 0 0 0 0 0':
    
    ans=0
    n=input()
    if n=='0 0 0 0 0 0':
        break
    l=list(map(int, n.split()))
    ans+=l[3]+l[4]+l[5]
    if l[2]%4!=0:
        ans+=l[2]//4+1
    else:
        ans+=l[2]//4
    e3=l[2]%4
    e4=l[3]
    e5=l[4]
    if e3!=0:
        l[1]-=e4*5+(7-2*e3)
        if l[1]>0:
            ans+=l[1]//9
            
            l[0]-=11*e5+8-e3
            l[0]-=(36-(l[1]%9)*4)
            if l[1]%9!=0:
                ans+=1
            else:
                l[0]+=36
                
            if l[0]>0:
                ans+=l[0]//36
                if l[0]%36!=0:
                    ans+=1
        else:
            l[0]-=11*e5+8-e3+(-l[1]*4)
            if l[0]>0:
                ans+=l[0]//36
                if l[0]%36!=0:
                    ans+=1
    else:
        l[1]-=e4*5
        if l[1]>0:
            ans+=l[1]//9
            l[0]-=11*e5
            l[0]-=(36-(l[1]%9)*4)
            if l[1]%9!=0:
                ans+=1
            else:
                l[0]+=36
            if l[0]>0:
                ans+=l[0]//36
                if l[0]%36!=0:
                    ans+=1
        else:
            l[0]-=11*e5+(-l[1]*4)
            if l[0]>0:
                ans+=l[0]//36
                if l[0]%36!=0:
                    ans+=1
    print(ans)
    
            
