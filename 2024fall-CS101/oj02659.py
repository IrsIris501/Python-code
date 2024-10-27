paras=list(map(int, input().split()))
a=paras[0]
b=paras[1]
k=paras[2]
field=[]
ans=0
for i in range(3*a):
    field.append([])
    field[i]=[1]*(3*b)
for i in range(k):
    l=list(map(int, input().split()))
    r=l[0]
    s=l[1]
    p=l[2]
    t=l[3]
    if t:
        for i in range(3*a):
            for j in range(3*b):
                if a+r-1-p//2<=i<a+r+p//2 and b+s-1-p//2<=j<b+s+p//2 and field[i][j]:
                    field[i][j]=1
                else:
                    field[i][j]=0
    else:
        for i in range(max(a+r-1-p//2, 0), min(3*a, a+r+p//2)):
            for j in range(max(0, b+s-1-p//2), min(3*b, b+s+p//2)):
                field[i][j]=0

for i in range(a, 2*a):
    ans+=field[i][b:2*b].count(1)

if ans==0:
    ans=a*b
print(ans)
    
