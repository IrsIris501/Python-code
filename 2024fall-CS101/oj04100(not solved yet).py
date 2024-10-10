
k=int(input())
for i in range(k):
    n=int(input())
    programs=[]
    time={}
    mintime=1000
    maxtime=0
    test=[]
    for i in range(len(program)):
        programs.append(list(map(int, input().split())))
        if programs[i][0]<mintime:
            mintime=programs[i][0]
        if programs[i][1]>maxtime:
            maxtime=programs[i][1]
    for i in range(mintime, maxtime+1):
        time[i]=0
    
    for i in programs:
        for j in range(i[0], i[1]+1):
            time[j]+=1
    occupy=time.items()
    occupy.sort(key=lambda x:x[1])
    
    
