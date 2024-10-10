n=int(input())
v=list(map(int, input().split()))
u=sorted(v)
V=[0]
U=[0]
for i in range(1, n+1):
    V.append(V[i-1]+v[i-1])
    U.append(U[i-1]+u[i-1])
m=int(input())
for i in range(m):
    l=list(map(int, input().split()))
    if l[0]==1:
        ans=V[l[2]]-V[l[1]-1]
    else:
        ans=U[l[2]]-U[l[1]-1]
    print(ans)
