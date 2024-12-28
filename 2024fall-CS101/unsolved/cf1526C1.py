from heapq import *
n=int(input())
a=list(map(int, input().split()))
heap=[]
health=0
for i in range(n):
    heappush(heap, a[i])
    health+=a[i]
    if health<0:
        health-=heappop(heap)
        
print(len(heap))
    
