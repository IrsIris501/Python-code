import itertools
t=[]
c=[i for i in range(1, 9)]
for i in itertools.permutations(c):
    if len(set(i[j]-j for j in range(8)))==len(set(i[j]+j for j in range(8)))==8:
        t.append(i)

n=int(input())
for i in range(n):
    s=int(input())
    print(*t[s-1], sep='')
