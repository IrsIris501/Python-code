n=int(input())
ss=[]
length=[]
ans=''
for i in range(n):
    s=input()
    ss.append(s)
    length.append(len(s))
m=min(length)
flag=1
for i in range(m):
    compare=ss[0][i]
    for j in ss:
        if j[i]!=compare:
            flag=0
            break
        else:
            if j==ss[-1]:
                ans+=compare
    if flag==0:
        break
print(ans)
    
