from collections import deque
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
def avail(nx, ny, time):
    if 0<=nx<r and 0<=ny<c and (maze[nx][ny]!="#" or (maze[nx][ny]=="#" and time%k==0)) and time%k not in visited[nx][ny]:
        return 1
    else:
        return 0

def bfs(maze, x, y):
    q=deque([(x, y, 0)])
    visited[x][y].append(0)
    
    while q:
        px, py, time=q.popleft()
        if maze[px][py]=="E":
            return time
        for i in range(4):
            nx=px+dx[i]
            ny=py+dy[i]
            if avail(nx, ny, time+1):
                q.append((nx, ny, time+1))
                visited[nx][ny].append((time+1)%k)
    return 0
t=int(input())
for _ in range(t):
     
    r, c, k=map(int, input().split())
    visited=[[[] for i in range(c)] for j in range(r)]
    maze=[]
    for i in range(r):
        maze.append(list(input()))
    flag=0
    for i in range(r):
        for j in range(c):
            if maze[i][j]=="S":
                x0=i
                y0=j
                flag=1
                break
        if flag:
            break
        
    a=bfs(maze, x0, y0)
    if a:
        print(a)
    else:
        print("Oop!")
