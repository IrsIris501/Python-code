n=int(input())
flag=1
for i in range(6, n):
    if n%i==0:
        print(n//i)
        flag=0
        break
if flag==1:
    print(1)
