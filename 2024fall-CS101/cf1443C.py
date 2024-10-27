t=int(input())
for i in range(t):
    n=int(input())
    a_list=list(map(int, input().split()))
    b=list(map(int, input().split()))
    a=[]
    for i in range(n):
        a.append((i, a_list[i]))
    a.sort(key=lambda x:x[1], reverse=True)
    ans=0
    for i in range(n):
        ans+=b[i]
    while a[-1][1]<ans:
        ans-=b[a[-1][0]]
        ans=max(ans, a[-1][1])
        a.pop(-1)
        if a==[]:
            break
    print(ans)
