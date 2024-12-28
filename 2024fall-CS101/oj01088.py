def avail(x, y, dx, dy):
    if 0<=x+dx<r and 0<=y+dy<c and maze[x+dx][y+dy]>maze[x][y]:
        return 1
    else:
        return 0
    
r, c=map(int, input().split())
maze=[]
for i in range(r):
    maze.append(list(map(int, input().split())))
stack=[]
for i in range(r):
    for j in range(c):
        stack.append((maze[i][j], i, j))
stack.sort(reverse=True)
dp=[[0 for i in range(c)] for j in range(r)]
di=[(1, 0), (0, 1), (-1, 0), (0, -1)]
for h, i, j in stack:
    flag=0
    for dx, dy in di:
        if avail(i, j, dx, dy):
            dp[i][j]=max(dp[i][j], dp[i+dx][j+dy]+1)
            flag=1
    if not flag:
        dp[i][j]=1
ans=0
for i in range(r):
    ans=max(ans, max(dp[i]))
print(ans)
