#연결요소의 갯수
#8.4풀이
import sys;p=sys.stdin.readline
from collections import deque
number=0
def bfs(v):
    visited[v]=True
    queue=deque()
    queue.append(v)
    while queue:
        v=queue.popleft()
        for i in graph[v]:
            if visited[i]==0:
                visited[i]=True
                queue.append((i))
n,m = map(int,p().rstrip().split())
n+=1
graph=[[]*n for i in range(n)] 
visited=[False]*n
for i in range(m):
    u,v=map(int,p().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(1,n):
    if visited[i]==0:
        number+=1
        bfs(i)
print(number)