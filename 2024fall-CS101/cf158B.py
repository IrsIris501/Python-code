import math
n=int(input())
a=list(map(int, input().split()))
numbers={}
for i in range(1, 5):
    numbers[i]=a.count(i)
ans=numbers[4]+numbers[3]
numbers[1]-=numbers[3]
if numbers[2]%2==0:
    ans+=numbers[2]//2
    if numbers[1]>0:
        ans+=math.ceil(numbers[1]/4)
else:
    ans+=numbers[2]//2+1
    numbers[1]-=2
    if numbers[1]>0:
        ans+=math.ceil(numbers[1]/4)
print(ans)
