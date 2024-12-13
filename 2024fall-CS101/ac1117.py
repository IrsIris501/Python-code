def win(a, b, n):
    if b==0:
        return n%2==1
    if a//b>=2:
        return n%2==0
    if win(b, a-b, n+1):
        return 1
    else:
        return 0
    
while True:
    c, d=map(int, input().split())
    if not c and not d:
        break
    a=max(c, d)
    b=min(c, d)
    if win(a, b, 0):
        print("win")
    else:
        print("lose")
