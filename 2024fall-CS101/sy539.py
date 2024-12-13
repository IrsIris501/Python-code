from math import sqrt
a=input()
def ispsquare(x):
    x=int(x)
    if x!=0 and int(sqrt(x))==sqrt(x):
        return 1
    else:
        return 0
    
lucky=False

def dfs(a, x):
    global lucky
    if ispsquare(x[a::]):
        lucky=True
        return
    for i in range(len(x)-1, a, -1):
        if ispsquare(x[a:i]):
            dfs(i, x)

dfs(0, a)
if lucky:
    print("Yes")
else:
    print("No")
            
