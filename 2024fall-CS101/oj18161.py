rowa, cola=input().split()
rowa=int(rowa)
cola=int(cola)
a=[]
for i in range(rowa):
    a.append(list(map(int, input().split())))
rowb, colb=input().split()
rowb=int(rowb)
colb=int(colb)
b=[]
for i in range(rowb):
    b.append(list(map(int, input().split())))
rowc, colc=input().split()
rowc=int(rowc)
colc=int(colc)
c=[]
for i in range(rowc):
    c.append(list(map(int, input().split())))
if rowc!=rowa or colb!=colc or cola!=rowb:
    print("Error!")
else:
    ans=[]
    for i in range(rowa):
        ans.append([])
        for j in range(colb):
            m=0
            for k in range(rowb):
                m+=a[i][k]*b[k][j]
            m+=c[i][j]
            ans[i].append(m)
    for i in range(rowa):
        for j in range(colb):
            if j!=colb-1:
                print(ans[i][j], end=' ')
            else:
                print(ans[i][j])
                
