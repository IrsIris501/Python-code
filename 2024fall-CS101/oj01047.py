def iscycle(s):
    j=[]
    flag=0
    l=len(s)
    ints=int(s)
    for i in range(l):
        a=int(s[i::]+s[0:i])
        j.append(a)
    j.sort()
    for i in range(1, l+1):
        if ints*i!=j[i-1]:
            flag=1
            break
    return flag
while True:
    try:
        s=input()
    except:
        break
    print(s+' is '+'not '*iscycle(s)+"cyclic")
