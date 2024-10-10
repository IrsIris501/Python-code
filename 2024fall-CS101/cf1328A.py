n=int(input())
for i in range(n):
    l=list(map(int, input().split()))
    if l[0]%l[1]==0:
        print(0)
    else:
        print(l[1]-l[0]%l[1])
        
