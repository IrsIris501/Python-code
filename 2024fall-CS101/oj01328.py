import math
i=0
while True:
    flag=0
    i+=1
    n, d=input().split()
    n=int(n)
    d=int(d)
    if n==d==0:
        break
    islands=[]
    for j in range(n):
        islands.append(list(map(int, input().split())))
    useless=input()
    ranges=[]
    for j in range(n):
        if islands[j][1]>d:
            print("Case "+str(i)+": -1")
            flag=1
            break
        p=islands[j][0]-math.sqrt(d*d-islands[j][1]**2)
        q=islands[j][0]+math.sqrt(d*d-islands[j][1]**2)
        ranges.append([p, q])
    if flag:
        continue
    ranges.sort(key=lambda x:x[1])
    s=ranges[0][0]-1
    ans=0
    for j in range(n):
        if ranges[j][0]>s:
            ans+=1
            s=ranges[j][1]
    print("Case "+str(i)+": "+str(ans))
    
    
