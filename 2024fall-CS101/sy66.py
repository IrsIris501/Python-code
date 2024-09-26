n=int(input())
for i in range(1, n+1):
    if i==n:
        print("*"*n)
    else:   
        for j in range(i):
            if j==i-1:
                print("*")
            elif j==0:
                print("*", end='')
            else:
                print(" ", end='')
