n=int(input())
l=list(map(int, input().split()))
s=set(l)
sbox=[]
for i in s:
    sbox.append([i, l.count(i)])
sbox.sort(key=lambda x:x[0])
ans=0
while sbox!=[]:
    if sbox[-1][1]>ans:
        k=sbox[-1][1]-ans
        ans+=k
    else:
        sbox.pop()
print(ans)
