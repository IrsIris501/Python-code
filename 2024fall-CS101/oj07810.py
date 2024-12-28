def judge(x):
    if x%19==0:
        return 0
    x=str(x)
    for i in range(1, len(x)):
        if x[i-1:i+1]=='19':
            return 0
    return 1
n=int(input())
for i in range(n):
    if judge(int(input())):
        print("No")
    else:
        print("Yes")
        
