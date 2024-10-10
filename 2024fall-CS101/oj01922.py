import math
while True:
    n=int(input())
    if n==0:
        break
    riders=[]
    for i in range(n):
        l=list(map(int, input().split('\t')))
        riders.append((l[0]/3.6, l[1], 4500*3.6/l[0]+l[1]))
    riders.sort(key=lambda x:x[1])
    depart_time=0
    arrive_time=100000
    for i in range(n):
        if riders[i][1]>=depart_time and riders[i][2]<arrive_time:
            arrive_time=riders[i][2]
    print(math.ceil(arrive_time))
    
