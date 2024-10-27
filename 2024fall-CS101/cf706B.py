n=int(input())
x=list(map(int, input().split()))
x.sort(reverse=True)
maxx=x[0]
anslist=[]
ans=0
for i in range(maxx+1):
    while i>=x[-1]:
        ans+=1
        x.pop(-1)
        if x==[]:
            break
    anslist.append(ans)
q=int(input())
for i in range(q):
    qi=int(input())
    if qi<=maxx:
        print(anslist[qi])
    else:
        print(anslist[-1])
