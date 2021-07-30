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
e,d=0,0
res=0

def dfs(v,depth):
  global e,d,res

  if(depth==5):
    res=1
    return

  if(depth>d):
    e=v
    d=depth

  for i in range(len(graph[v])):
    if not visited[graph[v][i]]:
      if res: break
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