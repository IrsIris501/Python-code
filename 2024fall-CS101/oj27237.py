from collections import deque
def avail(x, inq):
    if x not in inq and x<50000:
        return 1
    else:
        return 0
def bfs(n, m):
    global path
    q=deque([(n, 0)])
    inq=set([n])
    while q:
        pos, step=q.popleft()
        if pos==m:
            return step
        if avail(3*pos, inq):
            q.append((3*pos, step+1))
            inq.add(3*pos)
            path[3*pos]=pos
        if avail(pos//2, inq):
            q.append((pos//2, step+1))
            inq.add(pos//2)
            path[pos//2]=pos
def find_path(path, n, m):
    pos=m
    s=''
    while True:
        if path[pos]*3==pos:
            s+="H"
            pos=path[pos]
        else:
            s+="O"
            pos=path[pos]
        if pos==n:
            break
    return s[::-1]
while True:
    n, m=map(int, input().split())
    if not n and not m:
        break
    path=["" for i in range(50000)]
    step=bfs(n, m)
    print(step)
    
    s=find_path(path, n, m)
    print(s)
