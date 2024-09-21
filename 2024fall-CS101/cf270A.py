n=int(input())
for i in range(n):
    a=float(input())
    a=180-a
    if 360%a==0:
        print("YES")
    else:
        print("NO")
