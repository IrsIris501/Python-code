m, n=input().split()
m=int(m)
n=int(n)
a=[]
for i in range(m, n+1):
    j=str(i)
    if int(j[0])**3+int(j[1])**3+int(j[2])**3==i:
        a.append(i)
if a!=[]:
    print(*a)
else:
    print("NO")

