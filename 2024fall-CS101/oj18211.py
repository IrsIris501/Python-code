p=int(input())
a=list(map(int, input().split()))
a.sort()
ans=0
while len(a)>1 or (a!=[] and p>=a[0]):
    if p>=a[0]:
        p-=a[0]
        a.pop(0)
        ans+=1
    elif ans>=1:
        p+=a[-1]
        a.pop(-1)
        ans-=1
    else:
        break
print(ans)


