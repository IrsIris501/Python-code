def is_squaretwoindex(a, b):
    tag=0
    if a==n-1:
        if b==m-1:
            if pixel[a-1][b-1]*pixel[a][b]*pixel[a-1][b]*pixel[a][b-1]==1:
                tag=1
        elif b==0:
            if pixel[a-1][b+1]*pixel[a-1][b]*pixel[a][b+1]*pixel[a][b]==1:
                tag=1
        else:
            if pixel[a-1][b-1]*pixel[a][b]*pixel[a-1][b]*pixel[a][b-1]==1:
                tag=1
            elif pixel[a-1][b+1]*pixel[a-1][b]*pixel[a][b+1]*pixel[a][b]==1:
                tag=1
    elif a==0:
        if b==m-1:
            if pixel[a+1][b-1]*pixel[a][b]*pixel[a+1][b]*pixel[a][b-1]==1:
                tag=1
        elif b==0:
            if pixel[a+1][b+1]*pixel[a+1][b]*pixel[a][b+1]*pixel[a][b]==1:
                tag=1
        else:
            if pixel[a+1][b-1]*pixel[a][b]*pixel[a+1][b]*pixel[a][b-1]==1:
                tag=1
            elif pixel[a+1][b+1]*pixel[a+1][b]*pixel[a][b+1]*pixel[a][b]==1:
                tag=1
    else:
        if b==m-1:
            if pixel[a+1][b-1]*pixel[a][b]*pixel[a+1][b]*pixel[a][b-1]==1:
                tag=1
            elif pixel[a-1][b-1]*pixel[a][b]*pixel[a-1][b]*pixel[a][b-1]==1:
                tag=1
        elif b==0:
            if pixel[a+1][b+1]*pixel[a+1][b]*pixel[a][b+1]*pixel[a][b]==1:
                tag=1
            elif pixel[a-1][b+1]*pixel[a-1][b]*pixel[a][b+1]*pixel[a][b]==1:
                tag=1
        else:
            if pixel[a+1][b-1]*pixel[a][b]*pixel[a+1][b]*pixel[a][b-1]==1:
                tag=1
            elif pixel[a+1][b+1]*pixel[a+1][b]*pixel[a][b+1]*pixel[a][b]==1:
                tag=1
            elif pixel[a-1][b+1]*pixel[a-1][b]*pixel[a][b+1]*pixel[a][b]==1:
                tag=1
            elif pixel[a-1][b-1]*pixel[a][b]*pixel[a-1][b]*pixel[a][b-1]==1:
                tag=1
    return tag
l=list(map(int, input().split()))
n=l[0]
m=l[1]
k=l[2]
if n==1 or m==1:
    print(0)
else:
    pixel=[]
    for i in range(n):
        pixel.append([])
        for j in range(m):
            pixel[i].append(0)
    flag=0
    for i in range(k):
        r, c=input().split()
        r=int(r)
        c=int(c)
        pixel[r-1][c-1]=1
        if is_squaretwoindex(r-1, c-1):
            flag=1
            print(i+1)
            break
        
    if flag==0:
        print(flag)
        
