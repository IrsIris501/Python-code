def ht(n, i, j, k):
    if n==1:
        print(i+"->"+k)
        return
    ht(n-1, i, k, j)
    ht(1, i, j, k)
    ht(n-1, j, i, k)
n=int(input())
a=[1]
for i in range(17):
    a.append(2*a[i]+1)
print(a[n-1])
ht(n, "A", 'B', 'C')
