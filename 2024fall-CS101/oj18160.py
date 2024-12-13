# pylint: skip-file
def valid(x, y):
    if 0<=x<n and 0<=y<m and not visited[x][y] and maze[x][y]=="W":
        return 1
    else:
        return 0

def skip(x, y):
    flag=0
    for i in range(8):
        nx=x+dx[i]
        ny=y+dy[i]
        if valid(nx, ny):
            flag=1
            break
    return flag

def dfs(maze, x, y):
    global cnt
    if not skip(x, y):
        return 
    for i in range(8):
        nx=x+dx[i]
        ny=y+dy[i]
        if valid(nx, ny):
            visited[nx][ny]=1
            cnt[-1]+=1
            dfs(maze, nx, ny)
            
dx=[1, 1, 1, 0, -1, -1, -1, 0]
dy=[1, -1, 0, 1, 1, -1, 0, -1]

t=int(input())

for _ in range(t):
    n, m=map(int, input().split())
    maze=[]
    cnt=[0]
    visited=[[0 for i in range(m)] for j in range(n)]
    
    for i in range(n):
        maze.append(list(input()))

    for i in range(n):
        for j in range(m):
            if maze[i][j]=='W' and not visited[i][j]:
                cnt.append(1)
                visited[i][j]=1
                dfs(maze, i, j)
    print(max(cnt))
