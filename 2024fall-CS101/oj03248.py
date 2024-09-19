while True:
    try:
        a, b=input().split()
    except:
        break
    a=int(a)
    b=int(b)
    flag=1
    if a<b:
        a, b=b, a
    if a%b==0:
        print(b)
        flag=0
    else:
        for i in range(2, b//2+1):
            if a%(b/i)==0:
                print(b//i)
                flag=0
                break
    if flag==1:
        print(1)
