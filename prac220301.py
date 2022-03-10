from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for i in range(n)]
# 상하좌우 탐색
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
count = 0
# def bfs(x,y):
#     #아이스크림을 만들 수 없는 공간인 경우 False를 반환

#     if graph[x][y]==1:
#         return False
#     q=deque()
#     q.append((x,y))
#     while q:
#         x,y=q.popleft()
#         graph[x][y]=1
#         for i in range(4):
#             nx=x+dx[i]
#             ny=y+dy[i]
#             if nx>=0 and nx<n and ny>=0 and ny<m and graph[nx][ny]==0:
#                 q.append((nx,ny))
#     return True
# for i in range(n):
#     for j in range(m):
#         if bfs(i,j)==True:
#             count+=1
# print(count)


def dfs(x, y):
    if x >= 0 and x < n and y >= 0 and y < m and graph[x][y] == 0:
        graph[x][y] = 1
        for v in range(4):
            dfs(x+dx[v], y+dy[v])
        return True
    return False

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            count += 1
print(count)
