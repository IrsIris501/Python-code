from copy import deepcopy
n, k=map(int, input().split())
t=list(map(int, input().split()))
t.sort(reverse=True)
at=0
while True:
    at+=len(t)*t[-1]/k
    tmp=deepcopy(t[-1])
    for i in range(len(t)):
        t[i]-=t[-1]
    
    while t[-1]<=0:
        t.pop(-1)
        if t==[]:
            break
    if t==[] or len(t)<k:
        break
print("%.3f" %at)
