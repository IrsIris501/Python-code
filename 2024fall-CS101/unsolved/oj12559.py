def abigger(a, b):
    if b!=a[:len(b)]:
        return 1
    else:
        while b==a[:len(b)]:
            a=a[len(b):]
        if a>b:
            return 1
        else:
            return 0
n=int(input())
s=input().split()
s.sort()
ansmax=''
ansmin=''
while len(s)>=2:
    if abigger(s[-1], s[-2]):
        ansmax+=s[-1]
        s.pop(-1)
    else:
        s[-1],s[-2]=s[-2],s[-1]
print(ansmax)
