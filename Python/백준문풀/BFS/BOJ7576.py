import sys;p=sys.stdin.readline
from collections import deque
res = 0 #결과값
queue=deque()
def bfs():
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if (0 <= nx < n) and (0 <= ny < m) and (graph[nx][ny] == 0):
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))
            
m,n=map(int,p().rstrip().split())#가로,세로
graph=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
for i in range(n):
    graph.append(list(map(int,p().rstrip().split())))
    for j in range(m):
        if graph[i][j]==1: #방문한 노드만 저장(익은 토마토의 좌표를 담음)
            queue.append((i,j))
bfs()
for i in graph:
    for j in i:
        if j==0:
            print(-1)
            sys.exit()
    res= max(res,max(i)) 
print(res-1)