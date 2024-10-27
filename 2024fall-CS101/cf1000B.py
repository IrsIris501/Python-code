n, m=input().split()
n=int(n)
m=int(m)
a=[0]
a+=list(map(int, input().split()))
a.append(m)
ss=[]
gap0=[]
gap1=[]
temp1=0
temp2=0
for i in range(1, n+2):
    ss.append(a[i]-a[i-1])
for i in range(n, -1, -1):
    gap1.append(temp1)
    gap0.append(temp2)
    if i%2:
        temp2+=ss[i]
    else:
        temp1+=ss[i]
gap1.append(temp1)
gap0.append(temp2)
gap1.reverse()
gap0.reverse()
#print(gap0, gap1, sep='\n')
ans=0
for i in range(n+2):
    if a[i]-1>0:
        if a[i-1]!=a[i]-1:
            if i%2:
                temp=-1+gap0[i]-gap1[i]
            else:
                temp=1+gap0[i]-gap1[i]
            if temp>ans:
                ans=temp
            #print(temp, '-')
    if a[i]+1<m:
        if a[i]+1!=a[i+1]:
            if i%2:
                temp=-1+gap0[i]-gap1[i]
            else:
                temp=1+gap0[i]-gap1[i]
            if temp>ans:
                ans=temp
            #print(temp, '+')
        
print(gap1[0]+ans)
