n, m=input().split()
n=int(n)
m=int(m)
stu=list(map(int, input().split()))
stu.sort()
diff=[]
for i in range(n-1):
    diff.append(stu[i+1]-stu[i])
diff.sort()
ans=0
for i in range(n-m):
    ans+=diff[i]
print(ans)
