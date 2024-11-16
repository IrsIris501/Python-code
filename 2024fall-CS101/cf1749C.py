from copy import deepcopy
def playgame(a, k):
    flag=1
    for i in range(k, 0, -1):
        if a==[]:
            flag=0
        else:
            for j in a:
                flag=0
                if j<=i:
                    a.remove(j)
                    flag=1
                    break
            if not flag:
                break
            if a!=[]:
                a.pop(-1)
    return flag

t=int(input())
for i in range(t):
    n=int(input())
    a=sorted(list(map(int, input().split())), reverse=True)
    b=a
    ans=0
    while True:
        if playgame(a, ans):
            ans+=1
            a=deepcopy(b)
            
        else:
            print(ans-1)
            break
