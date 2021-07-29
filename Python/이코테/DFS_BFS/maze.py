
#미로탈출
from collections import deque
#나의 코드 
#불안정함,멍청한 코드

# def bfs():
#   queue=deque([[0,0]])#시작점을 큐에 삽입 
#   while queue:
#     v1,v2= queue.popleft()#현재노드
#     if v1>-1 and v1<N and v2>-1 and v2<M: 
#       if v1==N-1 and v2==M-1 :
#         visited[v1][v2]=True
#         break;
#       if graph[v1][v2]==1:
#         visited[v1][v2]=True
#         queue.append([v1,v2+1])
#         queue.append([v1+1,v2])
# N,M = map(int,input().split())
# graph=[]
# for i in range(N):
#   graph.append(list(map(int,input())))
# visited = [[False]*M for _ in range(N)]
# result=0
# bfs()
# for i in range(N):
#   for j in range(M):
#     if visited[i][j]==True:
#       print(i+1,j+1)
#       result+=1
# print(result)


#나동빈님의 코드 , 안정적이다.
#비용을 더해가면서, 최종 목적지에 도착한 값중
def bfs(x,y):
  queue=deque()
  queue.append((x,y))
  while queue:
    x,y=queue.popleft()
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
      if nx< 0 or nx>=n or ny<0 or ny>=m:
        continue
      if graph[nx][ny]==0:
        continue
      if graph[nx][ny]==1:#방문한 노드는 이미 값이 즈
       
        graph[nx][ny] =graph[x][y]+1
        queue.append((nx,ny))
  return graph[n-1][m-1]
n,m =map(int,input().split())
graph=[]
for i in range(n):
  graph.append(list(map(int,input())))
#이동방향 정의
dx=[-1,1,0,0]
dy=[0,0,-1,1]
print(bfs(0,0))

