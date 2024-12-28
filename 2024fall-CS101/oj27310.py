def judge(pos):
    n=len(pos)
    if [] in pos:
        return 0
    if n==1:
        return 1
    elif n==2:
        for i in pos[0]:
            for j in pos[1]:
                if i!=j:
                    return 1
    elif n==3:
        for i in pos[0]:
            for j in pos[1]:
                for k in pos[2]:
                    if i!=j and i!=k and j!=k:
                        return 1
    else:
        for i in pos[0]:
            for j in pos[1]:
                for k in pos[2]:
                    for l in pos[3]:
                        if len(set([i, j, k, l]))==4:
                            return 1
    return 0
n=int(input())
a=[]
for i in range(4):
    a.append(list(set(input())))
for _ in range(n):
    s=list(input())
    pos=[]
    for i in range(len(s)):
        pos.append([])
        for j in range(4):
            if s[i] in a[j]:
                pos[i].append(j)
    pos.sort(key=lambda x:len(x))
    if judge(pos):
        print("YES")
    else:
        print("NO")
