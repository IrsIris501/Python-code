# pylint: skip-file
from collections import deque
import sys
# Constants
MAXD = 4
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# Functions
def can_visit(x, y, w):
    return 0 <= x < m and 0 <= y < n and matrix[x][y] < w and not in_queue[x][y]

def bfs(x, y, w):
    global safe
    global in_queue
    q = deque([(x, y)])
    in_queue[x][y] = True
    while q:
        front = q.popleft()
        if front==hq:
            safe=0
            return 
        for i in range(MAXD):
            next_x = front[0] + dx[i]
            next_y = front[1] + dy[i]
            if can_visit(next_x, next_y, w):
                in_queue[next_x][next_y] = True
                q.append((next_x, next_y))


lines=list(sys.stdin.read().split())

k=int(lines[0])
id=1
for _ in range(k):
    # Input
    safe=1
    m, n=map(int,(lines[id],lines[id+1]))
    id+=2
    matrix=[]
    for i in range(m):
        matrix.append(list(map(int,lines[id:id+n])))
        id+=n
    hq=(int(lines[id])-1,int(lines[id+1])-1)
    id+=2
    p=int(lines[id])
    id+=1
    water=[]
    for i in range(p):
        water.append((int(lines[id]),int(lines[id+1])))
        id+=2
    
    
    
    in_queue = [[False for i in range(n)] for j in range(m)]

    # Main process
    for i in range(p):
        if not in_queue[water[i][0]-1][water[i][1]-1]:
            bfs(water[i][0]-1, water[i][1]-1, matrix[water[i][0]-1][water[i][1]-1])

    # Output
    if safe:
        print("No")
    else:
        print("Yes")
