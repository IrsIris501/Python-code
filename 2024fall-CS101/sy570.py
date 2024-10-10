ans=["No", "Yes"]
n, q=input().split()
n=int(n)
flag=0
q=int(q)
relations=[]
for i in range(n):
    relations.append([])
for i in range(q):
    r=list(map(int, input().split()))
    relations[r[0]-1].append(r[1]-1)
for i in range(n):
    for j in relations[i]:
        for k in relations[j]:
            if i in relations[k]:
                flag=1
                break
        if flag==1:
            break
    if flag==1:
        break
print(ans[flag])
    
