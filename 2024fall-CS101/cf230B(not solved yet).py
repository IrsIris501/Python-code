p=[2, 3]
n=int(input())
l=list(map(int, input().split()))
for i in range(4, int(max(l)**0.5)+1):
    isprime=1
    t=i%6
    if t==1 or t==5:
        for j in range(2, int(i**0.5)+1):
            if i%j==0:
                isprime=0
    else:
        isprime=0
    if isprime==1:
        p.append(i)


for i in l:
    if int(i**0.5)==i**0.5:
        a=int(i**0.5)
        if a in p:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
