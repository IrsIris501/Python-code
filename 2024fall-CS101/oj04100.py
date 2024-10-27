k=int(input())
for i in range(k):
    n=int(input())
    programs=[]
    ans=0
    for j in range(n):
        programs.append(list(map(int, input().split())))
    programs.sort(key=lambda x:x[1])
    s=programs[0][0]-1
    for j in range(n):
        if programs[j][0]>s:
            ans+=1
            s=programs[j][1]
    print(ans)
    
    
