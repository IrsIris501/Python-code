n, q=input().split()
n=int(n)
q=int(q)
pairs=[]
for i in range(q):
    a, b=input().split()
    a=int(a)
    b=int(b)
    pairs.append((a+b, a*b))
if len(set(pairs))<len(pairs):
    print("Yes")
else:
    print("No")
