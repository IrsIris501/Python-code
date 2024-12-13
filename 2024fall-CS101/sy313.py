dx=[0, 1, 0, -1]
dy=[1, 0, -1, 0]
n, m=map(int, input().split())

cnt=0

def dfs(maze, x, y):
    global cnt
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if maze[nx][ny]=='e':
            cnt+=1
            continue
        if maze[nx][ny]==0:
            maze[x][y]=1
            dfs(maze, nx, ny)
            maze[x][y]=0
    return
    
maze=[]
maze.append([-1 for _ in range(m+2)])

for i in range(n):
    maze.append([-1]+list(map(int, input().split()))+[-1])

maze.append([-1 for _ in range(m+2)])
maze[1][1]='s'
maze[n][m]='e'
dfs(maze, 1, 1)
print(cnt)
