n=int(input())
a=list(map(int, input().split()))
ai=[]
for i in range(n):
    ai.append((i, a[i]))
ai.sort(key=lambda x:x[1])
outputl=[]
for i in range(n):
    outputl.append(ai[i][0]+1)
print(*outputl)
w=[]
temp=0
for i in range(n):
    w.append(temp)
    temp+=ai[i][1]
ans=sum(w)/n
print('%.2f' %ans)
