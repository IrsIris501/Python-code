s=input()
m=int(input())
a=[0]*len(s)
for i in range(len(s)-1):
    a[i+1]=a[i]+(s[i]==s[i+1])

for i in range(m):
    l, r=input().split()
    l=int(l)
    r=int(r)
    print(a[r-1]-a[l-1])
