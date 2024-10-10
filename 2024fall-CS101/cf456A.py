n=int(input())
a={}
for i in range(n):
    l=list(map(int, input().split()))
    a[l[0]]=l[1]
pq=sorted(a.items(), key=lambda x: x[0])
flag=1
for i in range(len(pq)-1):
    if pq[i][1]>pq[i+1][1]:
        flag=0
        break
if flag==0:
    print("Happy Alex")
else:
    print("Poor Alex")
