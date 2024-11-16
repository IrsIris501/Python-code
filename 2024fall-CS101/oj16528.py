
n=int(input())
ac=[]
for i in range(n):
    ac.append(list(map(int, input().split())))
ans=[0]

for i in range(62):
    temp=[]
    for j in ac:
        if j[1]==i:
            temp.append(ans[j[0]]+1)
    if temp!=[]:
        ans.append(max(max(temp), ans[-1]))
    else:
        ans.append(ans[-1])
print(ans[-1])

