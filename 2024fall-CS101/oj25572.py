from collections import deque
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
def final(cor):
    if maze[cor[0]][cor[1]]==9 or maze[cor[0]+mode][cor[1]+1-mode]==9:
        return 1
    else:
        return 0
def avail(cor, inq):
    if 0<=cor[0]<n and 0<=cor[1]<n and 0<=cor[0]+mode<n and 0<=cor[1]+1-mode<n and maze[cor[0]][cor[1]]!=1 and maze[cor[0]+mode][cor[1]+1-mode]!=1 and cor not in inq:
        return 1
    else:
        return 0
def bfs(scor, mode):
    q=deque([scor])
    inq=set([scor])
    while q:
        cor=q.popleft()
        if final(cor):
            return 1
        for i in range(4):
            nx=cor[0]+dx[i]
            ny=cor[1]+dy[i]
            if avail((nx, ny), inq):
                q.append((nx, ny))
                inq.add((nx, ny))
    return 0
n=int(input())
maze=[]
for i in range(n):
    maze.append(list(map(int, input().split())))
tscor=[]
for i in range(n):
    for j in range(n):
        if maze[i][j]==5:
            tscor.append((i, j))
if tscor[1][0]-tscor[0][0]==1:
    mode=1
else:
    mode=0
scor=tscor[0]
if bfs(scor, mode):
    print("yes")
else:
    print("no")
    
