#백준 1260번 문제 풀이
from collections import deque
def dfs(v):
  visited[v]=True
  print(v,end=" ")
  for i in graph[v]:
    if not visited[i]:
      dfs(i)

def bfs(v):
  visited[v]=True
  queue=deque([v])
  while queue:
    v=queue.popleft()
    print(v,end=" ")
    for i in graph[v]:
        if not visited[i]:
          queue.append(i)
          visited[i]=True
          
          
n,m,v=map(int,input().split())
graph=[[] for _ in range(n+1)] #n:정점의 개수 , m: 간선의 개수, v : 탐색을 시작하는 정점의 번호
for i in range(m):
  a,b=map(int,input().split())
  #인접리스트 생성(양방향)
  graph[a].append(b)
  graph[b].append(a)
for i in range(n+1):
  graph[i].sort() #작은 노드부터 탐색 


visited=[False]*(n+1)
dfs(v)
print()
visited=[False]*(n+1)
bfs(v)
print()