n, m=input().split()
n=int(n)
m=int(m)
bulbs=[]
for i in range(1, m+1):
    bulbs.append(i)
for i in range(n):
    s=list(map(int, input().split()))
    for j in range(1, len(s)):
        if s[j] in bulbs:
            bulbs.remove(s[j])
if bulbs==[]:
    print("YES")
else:
    print("NO")
