#미로탐색 문제
import sys
from collections import deque
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<m and graph[nx][ny]=='1':
                graph[nx][ny]=int(graph[x][y])+1
                queue.append((nx,ny))
    return graph[n-1][m-1] 
n,m = map(int,input().split())
graph=[list(input()) for _ in range(n)]
print(bfs(0,0))
for i in range(n):
    print(graph[i])
