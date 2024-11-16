d=int(input())
n=int(input())
x=[]
y=[]
t=[]
for i in range(n):
    a, b, c=map(int, input().split())
    x.append(a)
    y.append(b)
    t.append(c)
ans=0
cnt=0
for i in range(1025):
    for j in range(1025):
        temp=0
        for k in range(n):
            if abs(x[k]-i)<=d and abs(y[k]-j)<=d:
                temp+=t[k]
        if temp>ans:
            ans=temp
            cnt=1
        elif temp==ans:
            cnt+=1
print(cnt, ans)
