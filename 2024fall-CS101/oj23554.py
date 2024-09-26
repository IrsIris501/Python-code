n=int(input())
a=list(map(int, input().split()))
a.sort()
b=[]
c=[]
for i in range(1, n+1):
    if i in a:
        a.remove(i)
    else:
        b.append(i)
print(*b)
print(*a)
