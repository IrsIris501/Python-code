from heapq import *
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
def avail(nx, ny):
    if 0<=nx<m and 0<=ny<n and maze[nx][ny]!="#" and (nx, ny) not in save:
        return 1
    else:
        return 0

m, n, p=map(int, input().split())
maze=[]
for i in range(m):
    a=input().split()
    maze.append([])
    for j in a:
        if j=="#":
            maze[i].append(j)
        else:
            maze[i].append(int(j))
for _ in range(p):
    x0, y0, x, y=map(int, input().split())
    if maze[x0][y0]=="#" or maze[x][y]=="#":
        print("NO")
    else:
        save=set()
        heap=[]
        flag=1
        heappush(heap, (0, x0, y0))
        while heap!=[]:
            l, px, py=heappop(heap)
            save.add((px, py))
            for i in range(4):
                nx=px+dx[i]
                ny=py+dy[i]
                if avail(nx, ny):
                    heappush(heap, (l+abs(maze[px][py]-maze[nx][ny]), nx, ny))
            if px==x and py==y:
                print(l)
                flag=0
                break
        if flag:
            print("NO")
        
        
