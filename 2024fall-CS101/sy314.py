n, m, k=map(int, input().split())
maze=[[-1 for _ in range(m+2)]]
for i in range(n):
    maze.append([-1]+list(map(int, input().split()))+[-1])
maze.append([-1 for i in range(m+2)])
dx=[1, 0, -1, 0]
dy=[0, 1, 0, -1]
canReach=False
maze[n][m]='e'
def dfs(maze, x, y, step):
    global canReach
    
    
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if maze[nx][ny]==0:
            maze[x][y]=1
            dfs(maze, nx, ny, step-1)
            maze[x][y]=0
        if step==1 and maze[nx][ny]=='e':
            canReach=True
            return
    
dfs(maze, 1, 1, k)
if canReach:
    print("Yes")
else:
    print("No")
