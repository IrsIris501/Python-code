s=list(map(int, input().split('+')))
s.sort()
for i in range(len(s)):
    if i!=0:
        print('+'+str(s[i]), end='')
    else:
        print(str(s[i]), end='')
