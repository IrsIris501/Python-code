def isprime(x):
    flag=1
    s=x%6
    if s==1 or s==5:
        for i in range(4, int(x**0.5)+2):
            if x%i==0:
                flag=0
                break
    else:
        flag=0
    return flag
s=int(input())
if s%2==1:
    print(2*(s-2))
else:
    for i in range(s//2):
        if isprime(s//2-i)*isprime(s//2+i)==1:
            print((s//2-i)*(s//2+i))
            break
