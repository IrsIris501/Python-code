n, m=map(int, input().split())
maze=[]
for i in range(n):
    maze.append(list(map(int, input().split())))
visited=[[0 for i in range(m)] for j in range(n)]
dx=[1, 0, -1, 0]
dy=[0, 1, 0, -1]
canReach=False
step=10000
def dfs(x, y, s):
    global canReach
    global step
    if maze[x][y]==1:
        canReach=True
        if s<step:
            step=s
        return
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and maze[nx][ny]!=2:
            visited[nx][ny]=1
            dfs(nx, ny, s+1)
            visited[nx][ny]=0

dfs(0, 0, 0)
if canReach:
    print(step)
else:
    print("NO")
