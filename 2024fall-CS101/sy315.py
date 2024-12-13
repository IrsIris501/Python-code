from copy import deepcopy
n, m=map(int, input().split())
maze=[[-101]*(m+2)]
for i in range(n):
    maze.append([-101]+list(map(int, input().split()))+[-101])
maze.append([-101]*(m+2))
dx=[1, 0, -1, 0]
dy=[0, 1, 0, -1]
maxv=float('-inf')

def dfs(maze, x, y, now):
    global maxv
    if x==n and y==m:
        if now>maxv:
            maxv=now
            return
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if maze[nx][ny]>=-100:
            a=deepcopy(maze[x][y])
            maze[x][y]=-101
            dfs(maze, nx, ny, now+a)
            maze[x][y]=a
    
dfs(maze, 1, 1, maze[n][m])
print(maxv)
