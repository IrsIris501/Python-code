import heapq
import collections

n=int(input())
outl=collections.defaultdict(int)
outr=collections.defaultdict(int)

leftb=[]
rightb=[]
heapq.heapify(leftb)
heapq.heapify(rightb)
for i in range(n):
    sgn, left, right=input().split()
    left, right=map(int, [left, right])
    if sgn=="+":
        heapq.heappush(leftb, -left)
        heapq.heappush(rightb, right)
    else:
        outl[-left]+=1
        outr[right]+=1
    
    flag1=1
    flag2=1
    while True:
        if leftb==[]:
            flag1=0
            break
        l=heapq.heappop(leftb)
        if not outl[l]:
            heapq.heappush(leftb, l)
            break
        outl[l]-=1
    while True:
        if rightb==[]:
            flag2=0
            break
        r=heapq.heappop(rightb)
        if not outr[r]:
            heapq.heappush(rightb, r)
            break
        outr[r]-=1
    if l+r<0 and flag1 and flag2:
        print("YES")
    else:
        print("NO")
    

    
        
