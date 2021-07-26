#BFS(너비 우선 탐색) / 그래프 상에서 가까운 노드부터 우선적으로 탐색 
#특징 : 큐(Queue) 자료구조 이용 
#각 간선의 비용이 동일한 경우, 최단거리를 구하는데에도 사용됨. 
from collections import deque #deque 자료형을 사용하기 위하여 패키지 import

#BFS 메소드 정의 
def bfs(graph,start,visited):
  #큐(Queue) 구현을 위해 deque 라이브러리 사용
  queue= deque([start])
  #현재 노드를 방문 처리
  visited[start] = True
  #큐가 빌 때까지 반복
  while queue:
    #큐에서 하나의 원소를 뽑아 출력하기
    v= queue.popleft() #원소 뽑기
    print(v,end=' ')
    #아직 방문하지 않은 인접한 원소들을 큐에 삽입
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i]=True
#각 노드가 연결된 정보를 표현 (2차원 리스트) #이해못함..
graph = [
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

#각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

#정의된 BFS함수 호출
bfs(graph,1,visited)
