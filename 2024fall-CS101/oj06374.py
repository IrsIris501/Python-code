n=int(input())
s=input().split()
c=0
for i in range(n-1):
    if c+len(s[i])<=80:
        print(s[i], end='')
        c+=len(s[i])
        if c+len(s[i+1])<=80:
            print(' ', end='')
            c+=1
        else:
            print()
            c=0
    else:
        print()
        print(s[i]+' ', end='')
        c=len(s[i])
        
if c+len(s[n-1])<=80:
    print(s[n-1], end='')
else:
    print()
    print(s[n-1], end='')
