n, m=map(int, input().split())
maze=[]
value=[]
for i in range(n):
    maze.append(list(map(int, input().split())))
for i in range(n):
    value.append(list(map(int, input().split())))

dx=[1, 0, -1, 0]
dy=[0, 1, 0, -1]
mv=float("-inf")
visited=[[0 for i in range(m)] for _ in range(n)]
visited[0][0]=1
def dfs(value, x, y, cv):
    global maze
    global mv
    if cv>mv and x==n-1 and y==m-1:
        mv=cv
        return
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m and not maze[nx][ny] and not visited[nx][ny]:
            visited[nx][ny]=1
            dfs(value, nx, ny, cv+value[nx][ny])
            visited[nx][ny]=0

dfs(value, 0, 0, value[0][0])
print(mv)
