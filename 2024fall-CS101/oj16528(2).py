def MaxNonoverlapInt(s):
    if s==[]:
        return 0
    s.sort()
    temppos=0
    cnt=0
    for i in range(1, len(s)):
        if s[temppos][1]>=s[i][0]:
            if s[temppos][1]>=s[i][1]:
                temppos=i
            cnt+=1
        else:
            temppos=i
    return len(s)-cnt

n=int(input())
s=[]
for i in range(n):
    s.append(list(map(int, input().split())))
print(MaxNonoverlapInt(s))
