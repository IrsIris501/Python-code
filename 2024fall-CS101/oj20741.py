from collections import deque
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]

def land(x, y, s):
    if 0<=x<n and 0<=y<m and maze[x][y]==1 and (x, y) not in s:
        return 1
    else:
        return 0
    
def bfsa(x, y, inp):
    p=deque()
    p.append((x, y))
    
    inp.add((x, y))
    while p:
        front=p.popleft()
        
        for i in range(4):
            nx=front[0]+dx[i]
            ny=front[1]+dy[i]
            
            if land(nx, ny, inp):
                inp.add((nx, ny))
                p.append((nx, ny))
    return

#Input    
n=int(input())
maze=[]
for i in range(n):
    maze.append(list(map(int, list(input()))))
m=len(maze[0])

#Find Two Islands
for i in range(n):
    flag=0
    for j in range(m):
        if maze[i][j]==1:
            inp1=set()
            bfsa(i, j, inp1)
            flag=1
            break
    if flag:
        break
for i in range(n):
    flag=0
    for j in range(m):
        if maze[i][j]==1 and (i, j) not in inp1:
            inp2=set()
            bfsa(i, j, inp2)
            flag=1
            break
    if flag:
        break

#Compute distance
inp1=list(inp1)
inp2=list(inp2)
tmp=[]
for a in inp1:
    x0=a[0]
    y0=a[1]
    for b in inp2:
        x=b[0]
        y=b[1]
        tmp.append(abs(x-x0)+abs(y-y0)-1)
print(min(tmp))


