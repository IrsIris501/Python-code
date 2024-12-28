from collective import deque
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
def bfs(pos, step):
    q=deque()
    q.append(pos)
    for i in range(4):
        if 
t=int(input())
for _ in range(t):
    r, c, k=map(int, input().split())
    maze=[]
    for i in range(r):
        maze.append(list(input().spplit()))
    for i in range(r):
        for j in range(c):
            if maze[i][j]=='S':
                start=(i, j)
            elif maze[i][j]=="E":
                end=(i, j)
    ans=bfs(start, 0)
    
                
