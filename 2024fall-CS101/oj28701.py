
n, k=map(int, input().split())
t=list(map(int, input().split()))
t.sort()
at=0
while t!=[] and t[-1]>sum(t)/k:
    t.pop()
    k-=1
print('%.3f' %(sum(t)/k))
    
 
