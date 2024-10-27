import math
n=int(input())
primes=[]
#numbers=[True for i in range(int(1e6+1))]
numbers=[True]*(10**6+1)
numbers[0]=False
numbers[1]=False
def sieve(numbers):
    for i in range(2, int(1e6+1)):
        if numbers[i]:
            primes.append(i)
        for j in range(len(primes)):
            if i*primes[j]>int(1e6):
                break
            numbers[i*primes[j]]=False
            if i%primes[j]==0:
                break
sieve(numbers)
l=list(map(int, input().split()))
for i in l:
    a=math.sqrt(i)
    if a.is_integer() and numbers[int(a)]:
        print("YES")
    else:
        print("NO")
