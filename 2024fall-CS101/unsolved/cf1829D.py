def ispower3(n):
    while n%3==0:
        n=n//3
    return n==1

n=int(input())
for i in range(n):
    a, m=map(int, input().split())
    if a<m:
        print("NO")
    elif a==m:
        print("YES")
    else:
        flag=0
        while m>=1:
            if a%m==0:
                s=a//m
                if ispower3(s):
                    print("YES")
                else:
                    print("NO")
                flag=1
                break
            else:
                m=m/2
        if not flag:
            print("NO")
