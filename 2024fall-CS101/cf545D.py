n=int(input())
l=list(map(int, input().split()))
l.sort()
wait=0
ans=0
for i in l:
    if i<wait:
        ans+=1
    else:
        wait+=i
print(n-ans)
