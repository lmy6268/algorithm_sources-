# import sys
# def dfs(v,depth):
#   if depth==4:
#     print(1)
#     sys.exit()
#   for i in graph[v]:
#     if not visited[i]:
#         repeat(i,depth+1)
# def repeat(i,depth):
#   visited[i] = True
#   dfs(i, depth)
#   visited[i] = False
# #사람 수와 친구 관계의 수 입력
# N,M=map(int,sys.stdin.readline().rstrip().split())
# #관계 입력
# graph=[[] for _ in range(N)]
# visited=[False]*N
# for i in range(M):
#   #값을 인접리스트 형식으로 저장
#   a,b=map(int,sys.stdin.readline().rstrip().split())
#   graph[a].append(b)
#   graph[b].append(a)
# for i in range(N):
#   repeat(i,0)
# print(0)

import sys
e,d=0,0 #e는 edge정보를 담고, d는 깊이의 정보를 담는 변수
res=0 #최종적으로 출력할 답을 담는 변수

def dfs(v,depth):
  global e,d,res #전역변수를 가져와 사용

  if(depth==5):#만약 깊이가 5라면 탈출
    res=1 #관계가 형성되므로 1을 출력
    return #함수 종료

  if(depth>d): #탐색 중에 더 깊이가 깊은 관계를 찾은 경우
    e=v #e 업데이트
    d=depth #d 업데이트 

  for i in range(len(graph[v])): #현재 노드가 가진 이웃 노드의 간선 수 만큼 루프
    if not visited[graph[v][i]]: #만약 현재노드의 이웃노드가 방문하지 않은 노드일 경우
      if res: break  #만약 res값이 1이라면 탐색 무시
      visited[v]=True 
      dfs(graph[v][i],depth+1)
      visited[v]=False


n,m=map(int,sys.stdin.readline().rstrip().split())
graph=[[] for _ in range(n)]
for i in range(m):
  #값을 인접리스트 형식으로 저장
  a,b=map(int,sys.stdin.readline().rstrip().split())
  graph[a].append(b)
  graph[b].append(a)
visited=[False]*n
visited[0]=True
dfs(0,1)
if res==0:
  visited=[False]*n
  visited[e]=True
  dfs(e,1)
print(res)