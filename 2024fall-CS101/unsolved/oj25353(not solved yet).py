n, d=input().split()
n=int(n)
d=int(d)
a=[]
for i in range(n):
    a.append(int(input()))
while a!=[]:
    maxv=0
    minv=int(1e9+1)
    minpop=int(1e9+1)
    for i in range(len(a)):
        maxv=max(a[i], maxv)
        minv=min(a[i], minv)
        if abs(a[i]-maxv)<=d and abs(a[i]-minv)<=d and a[i]<minpop:
            minpop=a[i]
    a.remove(minpop)
    print(minpop)
            

