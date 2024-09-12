p=[2]
for i in range(1,1000):
    a=2*i+1
    flag=1
    for j in p:
        if a%j==0:
            flag=0
            break
    if flag==1:
        p.append(a)
n=int(input())
if n>=6 and n%2==0:
    for i in p:
        if i>n/2:
            break
        elif n-i in p:
            print(str(n)+'='+str(i)+'+'+str(n-i))
else:
    print("Error!")
