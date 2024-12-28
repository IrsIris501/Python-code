# 计概Cheat Sheet

Edited 20241123 1549

## 1. oj有自定义函数时出现奇怪的compile error

在代码第一行加

```python
# pylint: skip-file
```

## 2. bfs模板

### 示例：sy319矩阵中的块

https://sunnywhy.com/sfbj/8/2/319

题目描述

现有一个 n*m 的矩阵，矩阵中的元素为`0`或`1`。然后进行如下定义：

1. 位置(x,y)与其上下左右四个位置 $(x,y + 1)、(x,y - 1)、(x + 1,y)、(x-1,y)$ 是相邻的；
2. 如果位置 (x1,y1) 与位置 (x2,y2) 相邻，且位置 (x2,y2) 与位置 (x3,y3) 相邻，那么称位置(x1,y1)与位置(x3,y3)也相邻；
3. 称个数尽可能多的相邻的`1`构成一个“块”。

求给定的矩阵中“块”的个数。

**输入**

第一行两个整数 n、m（$2 \le n \le 100, 2 \le m \le 100$），分别表示矩阵的行数和列数；

接下来 n 行，每行 m 个`0`或`1`（用空格隔开），表示矩阵中的所有元素。

**输出**

输出一个整数，表示矩阵中“块”的个数。

样例1

输入

```
6 7
0 1 1 1 0 0 1
0 0 1 0 0 0 0
0 0 0 0 1 0 0
0 0 0 1 1 1 0
1 1 1 0 1 0 0
1 1 1 1 0 0 0
```

输出

```
4
```

解释

矩阵中的`1`共有`4`块，如下图所示。

![矩阵中的块_样例.png](https://raw.githubusercontent.com/GMyhf/img/main/img/202311262246785.png)



#### 加保护圈，inq_set集合判断是否入过队

```python
from collections import deque

# Constants
MAXD = 4
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    q = deque([(x, y)])
    inq_set.add((x,y))
    while q:
        front = q.popleft()
        for i in range(MAXD):
            next_x = front[0] + dx[i]
            next_y = front[1] + dy[i]
            if matrix[next_x][next_y] == 1 and (next_x,next_y) not in inq_set:
                inq_set.add((next_x, next_y))
                q.append((next_x, next_y))

# Input
n, m = map(int, input().split())
matrix=[[-1]*(m+2)]+[[-1]+list(map(int,input().split()))+[-1] for i in range(n)]+[[-1]*(m+2)]
inq_set = set()

# Main process
counter = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        if matrix[i][j] == 1 and (i,j) not in inq_set:
            bfs(i, j)
            counter += 1

# Output
print(counter)
```



#### inq 数组，结点是否已入过队

```python
from collections import deque

# Constants
MAXN = 100
MAXD = 4
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# Functions
def can_visit(x, y):
    return 0 <= x < n and 0 <= y < m and matrix[x][y] == 1 and not in_queue[x][y]

def bfs(x, y):
    q = deque([(x, y)])
    in_queue[x][y] = True
    while q:
        front = q.popleft()
        for i in range(MAXD):
            next_x = front[0] + dx[i]
            next_y = front[1] + dy[i]
            if can_visit(next_x, next_y):
                in_queue[next_x][next_y] = True
                q.append((next_x, next_y))

# Input
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
in_queue = [[False] * MAXN for _ in range(MAXN)]

# Main process
counter = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1 and not in_queue[i][j]:
            bfs(i, j)
            counter += 1

# Output
print(counter)

```

## 3. dfs模板

### 示例：sy314指定步数的迷宫问题 中等

https://sunnywhy.com/sfbj/8/1/314

现有一个 n*m 大小的迷宫，其中`1`表示不可通过的墙壁，`0`表示平地。每次移动只能向上下左右移动一格（不允许移动到曾经经过的位置），且只能移动到平地上。现从迷宫左上角出发，问能否在恰好第步时到达右下角。

**输入**

第一行三个整数$n、m、k \hspace{1em} (2 \le n \le5, 2 \le m \le 5, 2 \le k \le n*m)$，分别表示迷宫的行数、列数、移动的步数；

接下来行，每行个整数（值为`0`或`1`），表示迷宫。

**输出**

如果可行，那么输出`Yes`，否则输出`No`。

样例1

输入

```
3 3 4
0 1 0
0 0 0
0 1 0
```

输出

```
Yes
```

解释

假设左上角坐标是(1,1)，行数增加的方向为增长的方向，列数增加的方向为增长的方向。

可以得到从左上角到右下角的步数为`4`的路径为：(1,1)=>(2,1)=>(2,2)=>(2,3)=>(3,3)。

样例2

输入

```
3 3 6
0 1 0
0 0 0
0 1 0
```

输出

```
No
```

解释

由于不能移动到曾经经过的位置，因此无法在恰好第`6`步时到达右下角。



#### 加保护圈，原地修改

```python
dx = [-1, 0, 1, 0]
dy = [ 0, 1, 0, -1]

canReach = False
def dfs(maze, x, y, step):
    global canReach
    if canReach:
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if maze[nx][ny] == 'e':
            if step==k-1:
                canReach = True
                return
            
            continue
            
        if maze[nx][ny] == 0:
            if step < k:
                maze[x][y] = -1
                dfs(maze, nx, ny, step+1)
                maze[x][y] = 0
    

n, m, k = map(int, input().split())
maze = []
maze.append( [-1 for x in range(m+2)] )
for _ in range(n):
    maze.append([-1] + [int(_) for _ in input().split()] + [-1])
maze.append( [-1 for x in range(m+2)] )

maze[1][1] = 's'
maze[n][m] = 'e'

dfs(maze, 1, 1, 0)
print("Yes" if canReach else "No")
```



#### 辅助visited空间

```python
MAXN = 5
n, m, k = map(int, input().split())
maze = []
for _ in range(n):
    row = list(map(int, input().split()))
    maze.append(row)

visited = [[False for _ in range(m)] for _ in range(n)]
canReach = False

MAXD = 4
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def is_valid(x, y):
    return 0 <= x < n and 0 <= y < m and maze[x][y] == 0 and not visited[x][y]

def DFS(x, y, step):
    global canReach
    if canReach:
        return
    if x == n - 1 and y == m - 1:
        if step == k:
            canReach = True
        return
    visited[x][y] = True
    for i in range(MAXD):
        nextX = x + dx[i]
        nextY = y + dy[i]
        if step < k and is_valid(nextX, nextY):
            DFS(nextX, nextY, step + 1)
    visited[x][y] = False

DFS(0, 0, 0)
print("Yes" if canReach else "No")

```

## 4. heapq

```
DESCRIPTION
    Heaps are arrays for which a[k] <= a[2*k+1] and a[k] <= a[2*k+2] for
    all k, counting elements from 0.  For the sake of comparison,
    non-existing elements are considered to be infinite.  The interesting
    property of a heap is that a[0] is always its smallest element.

    Usage:

    heap = []            # creates an empty heap
    heappush(heap, item) # pushes a new item on the heap
    item = heappop(heap) # pops the smallest item from the heap
    item = heap[0]       # smallest item on the heap without popping it
    heapify(x)           # transforms list into a heap, in-place, in linear time
    item = heappushpop(heap, item) # pushes a new item and then returns
                                   # the smallest item; the heap size is unchanged
    item = heapreplace(heap, item) # pops and returns smallest item, and adds
                                   # new item; the heap size is unchanged

    Our API differs from textbook heap algorithms as follows:

    - We use 0-based indexing.  This makes the relationship between the
      index for a node and the indexes for its children slightly less
      obvious, but is more suitable since Python uses 0-based indexing.

    - Our heappop() method returns the smallest item, not the largest.

    These two make it possible to view the heap as a regular Python list
    without surprises: heap[0] is the smallest item, and heap.sort()
    maintains the heap invariant!

FUNCTIONS
    heapify(heap, /)
        Transform list into a heap, in-place, in O(len(heap)) time.

    heappop(heap, /)
        Pop the smallest item off the heap, maintaining the heap invariant.

    heappush(heap, item, /)
        Push item onto heap, maintaining the heap invariant.

    heappushpop(heap, item, /)
        Push item on the heap, then pop and return the smallest item from the heap.

        The combined action runs more efficiently than heappush() followed by
        a separate call to heappop().

    heapreplace(heap, item, /)
        Pop and return the current smallest value, and add the new item.

        This is more efficient than heappop() followed by heappush(), and can be
        more appropriate when using a fixed-size heap.  Note that the value
        returned may be larger than item!  That constrains reasonable uses of
        this routine unless written as part of a conditional replacement:

            if item > heap[0]:
                item = heapreplace(heap, item)

    merge(*iterables, key=None, reverse=False)
        Merge multiple sorted inputs into a single sorted output.

        Similar to sorted(itertools.chain(*iterables)) but returns a generator,
        does not pull the data into memory all at once, and assumes that each of
        the input streams is already sorted (smallest to largest).

        >>> list(merge([1,3,5,7], [0,2,4,8], [5,10,15,20], [], [25]))
        [0, 1, 2, 3, 4, 5, 5, 7, 8, 10, 15, 20, 25]

        If *key* is not None, applies a key function to each element to determine
        its sort order.

        >>> list(merge(['dog', 'horse'], ['cat', 'fish', 'kangaroo'], key=len))
        ['dog', 'cat', 'fish', 'horse', 'kangaroo']

    nlargest(n, iterable, key=None)
        Find the n largest elements in a dataset.

        Equivalent to:  sorted(iterable, key=key, reverse=True)[:n]

    nsmallest(n, iterable, key=None)
        Find the n smallest elements in a dataset.

        Equivalent to:  sorted(iterable, key=key)[:n]

```

## 5. 欧拉筛

O(n)

```python
import math
n=int(input())
primes=[]
#numbers=[True for i in range(int(1e6+1))]
numbers=[True]*(10**6+1)
numbers[0]=False
numbers[1]=False
def sieve(numbers):
    for i in range(2, int(1e6+1)):
        if numbers[i]:
            primes.append(i)
        for j in range(len(primes)):
            if i*primes[j]>int(1e6):
                break
            numbers[i*primes[j]]=False
            if i%primes[j]==0:
                break
sieve(numbers)
```

## 6. Dijkstra

Dijkstra 用来处理图中的最短路径问题

例：走山路

```python
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
```

## 7. dp

###### 7.1 01背包

例：采药

```python
v=int(input())
n=int(input())
item=[]
for i in range(n):
    item.append(int(input()))
dp=[[i for i in range(v+1)] for j in range(n+1)]
for i in range(1, n+1):
    for j in range(1, v+1):
        if j>=item[i-1]:
            dp[i][j]=min(dp[i-1][j], dp[i-1][j-item[i-1]])
        else:
            dp[i][j]=dp[i-1][j]
print(dp[-1][-1])


```

### dp

#### 最长公共子序列

```python
#子序列不一定连续
a=list(input())
b=list(input())
dp=[[0 for i in range(len(b))] for j in range(len(a))]
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
print(dp[-1][-1])
```

#### 最长单调增子序列

```python
a=list(map(int, input().split()))
n=len(a)
dp = [1]*n
for i in range(1,n):
    for j in range(i):
        if a[j]<a[i]:
            dp[i] = max(dp[i],dp[j]+1)
ans = max(dp)
print(ans)
```

#### 背包问题

##### 0-1背包

考虑取前i个物品用t时间所能得到的最大值，枚举第i个物品是否取完成转移。注意这里**加上时间参数t**，因为转移过程中t的限定可能会变。“加参数”是DP问题中最重要的技巧之一。

```python
dp = [0]*T
for i in range(n):
    for t in range(T,time[i]-1,-1):
        dp[t] = max(dp[t],dp[t-time[i]]+value[i])
ans = dp[T]
```

这里采用“**滚动数组**”的方法将二维数组压缩成一维，是DP问题中常用的技巧。这基于选前i个物品的状态仅依赖于选前i-1个物品的状态。注意**内层循环要倒着遍历**！

##### 完全背包

将0-1背包中内层循环改为正着遍历即可（这里其实就利用了**先前已经得到的信息**来简化转移：在先前的转移中物品i可能已经用过若干次了）

**多重背包**

最简单的思路是将多个同样的物品看成多个不同的物品，从而化为0-1背包。稍作优化：可以改善拆分方式，譬如将m个1拆成x_1,x_2,……,x_t个1，只需要这些x_i中取若干个的和能组合出1至m即可。最高效的拆分方式是尽可能拆成2的幂，也就是所谓“二进制优化”

```python
dp = [0]*T
for i in range(n):
    all_num = nums[i]
    k = 1
    while all_num>0:
        use_num = min(k,all_num) #处理最后剩不足2的幂的情形
        for t in range(T,use_num*time[i]-1,-1):
            dp[t] = max(dp[t-use_num*time[i]]+use_num*value[i],dp[t])
        k *= 2
        all_num -= use_num
```

注：背包问题的DP解法需要时间T不太大，因为要遍历每个可能的T。如果T很大而物品数量很少，采用DFS枚举物品的选法有时是更好的选择。

## 8. 二分查找

#### bisect库

python内置二分查找工具

注意bisect库只适用于**升序序列**，对于降序序列需要将列中每个数取相反数再使用；如果要按指定的key排序，可以将每个元素变为元组，把key放到元组的第一个形成元组序列（这种方法在接下来的单调队列优化中也有应用）

bisect_left和bisect_right分别表示插入可能位置中最靠左/右的位置；注意返回的是下标。

insort函数实现插入功能，原地修改列表而不返回值；但是**它是O(n)的**！

```python
import bisect
bisect.bisect_right(a,6)#返回在a列表中若要插入6的index（有重复数字会插在右边）
bisect.insort(a,6)#返回插入6后的列表a
```

#### 应用

一是方程求解问题。注意这个时候while循环的退出条件应当是l和r的差小于所需精度。

二是一类最优化问题，特别是“最值的最值”问题。这类问题所求的最优值通常具有”单调性质“，即小于某个数的都可以但大于它的都不行。对于这种问题，可以考虑**直接去枚举**最优值的可能取值。利用单调性质采用二分算法，这一步只有logn的复杂度；接下来的问题转化为**判断该最优值**是否满足要求。这样就把最优化问题转化为了判定问题，而判定问题有时有比较好的办法解决。所谓“0-1分数规划问题”也能用类似方法解决。

快速堆猪

![a55e3ca8d062425be2f4f2fdc042556](C:\Users\Eric_\Documents\WeChat Files\wxid_e310qs65ar3o22\FileStorage\Temp\a55e3ca8d062425be2f4f2fdc042556.jpg)
