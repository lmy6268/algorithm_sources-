import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for i in range(n)]
# 상하좌우 탐색
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
count = 0
def bfs(x,y):
    q=deque()
    q.append((x,y))
    while q:
        x,y=q.popleft()
        for v in range(4):
            nx=x+dx[v]
            ny=y+dy[v]
            if nx>=0 and nx<n and ny>=0 and ny<m and graph[nx][ny]==1:
                q.append((nx,ny))
                graph[nx][ny]=graph[x][y]+1 #핵심!!! 
    return graph[n-1][m-1]
print(bfs(0,0))
print(count,graph)



