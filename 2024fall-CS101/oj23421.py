def bag(p, w, i, b):
    if i==len(p)-1:
        if b>=w[-1]:
            return p[-1]
        else:
            return 0
    if b-w[i]<0:
        a=bag(p, w, i+1, b)
    else:
        a=max(bag(p, w, i+1, b-w[i])+p[i], bag(p, w, i+1, b))
    return a
n, b=map(int, input().split())
p=list(map(int, input().split()))
w=list(map(int, input().split()))
print(bag(p, w, 0, b))
