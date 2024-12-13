n, m=map(int, input().split())
maze=[]
for i in range(n):
    maze.append(list(map(int, input().split())))
visited=[[0 for _ in range(m)] for i in range(n)]
maxPath=[]
maxValue=-float("inf")
dx=[1, 0, -1, 0]
dy=[0, 1, 0, -1]
def dfs(x, y, currentPath, currentValue):
    global maxPath
    global maxValue
    if x==n-1 and y==m-1 and currentValue>maxValue:
        maxPath=currentPath[:]
        maxValue=currentValue
        return
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
            visited[nx][ny]=1
            currentPath.append((nx, ny))
            dfs(nx, ny, currentPath, currentValue+maze[x][y])
            visited[nx][ny]=0
            currentPath.pop()

visited[0][0]=1
dfs(0, 0, [(0, 0)], 0)
for i in range(len(maxPath)):
    print(maxPath[i][0]+1, maxPath[i][1]+1)
