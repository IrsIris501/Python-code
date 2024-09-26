useless=input()
l=list(map(int, input().split()))
flag=1
for i in range(1, len(l)):
    if l[i]<l[i-1]:
        flag=0
        break
if flag==1:
    print("YES")
else:
    print("NO")
