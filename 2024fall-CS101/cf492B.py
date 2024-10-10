n, l=input().split()
n=int(n)
l=int(l)
lanterns=list(map(int, input().split()))
lanterns.sort()
maxd=0
for i in range(1, n):
    if lanterns[i]-lanterns[i-1]>maxd:
        maxd=lanterns[i]-lanterns[i-1]
print(max(maxd/2, lanterns[0], l-lanterns[-1]))
