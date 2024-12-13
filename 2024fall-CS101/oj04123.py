# pylint: skip-file
def full2d(x):
    for i in range(len(x)):
        if 0 in x[i]:
            return 0
    return 1
def dfs(x, y, visited):
    global cnt
    if full2d(visited):
        cnt+=1
        return
    for i in range(8):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
            visited[nx][ny]=1
            dfs(nx, ny, visited)
            visited[nx][ny]=0
            
t=int(input())
dx=[1, 2, 2, 1, -1, -2, -2, -1]
dy=[2, 1, -1, -2, -2, -1, 1, 2]

for _ in range(t):
    cnt=0
    n, m, x, y=map(int, input().split())
    visited=[[0 for _ in range(m)] for i in range(n)]
    visited[x][y]=1
    dfs(x, y, visited)
    print(cnt)
