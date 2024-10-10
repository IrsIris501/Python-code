n=int(input())
if n%15==0:
    print(3*n)
else:
    if n%3==0:
        if (3*n)%5==1:
            print(3*n-6)
        else:
            print(3*n-(3*n)%5)
    elif n%3==1:
        if (3*n)%5==1:
            print(3*n-6)
        elif (3*n)%5==0:
            print(3*n-5)
        else:
            print(3*n-(3*n)%5)
    else:
        if (3*n)%5==2:
            print(3*n-12)
        elif (3*n)%5==0:
            print(3*n-5)
        else:
            print(3*n-(3*n)%5)
