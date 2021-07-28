# 문제 목적: connected component를 찾는게 목적
#벌써 어렵다...

#DFS로 특정 노드를 방문하고 연결돈 모든 노드들도 방문
def dfs(x,y):
  #주어진 범위를 벗어나는 경우에는 즉시 종료
  if x<=-1 or x>=N or y<=-1 or y>=M:
    return False
  #현재 노드를 방문하지 않았다면
  if graph[x][y] ==0:
    #해당 노드 방문 처리
    graph[x][y]=1
    #현재 노드의 상,하,좌,우 노드들도 재귀를 통해 호출
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x+1,y)
    dfs(x,y+1)
    return True
  return False


N,M = map(int,input().split()) #N: 세로 , M: 가로
graph=[]
#visited = [[False]* M for _ in range(N)]
#얼음틀 입력을 받음
'''for i in range(N): 
  a=input()
  itr=0
  for j in a:
    map[i][itr]=int(j)
    itr+=1
'''
for i in range(N):
  graph.append(list(map(int,input())))
#모든 노드에 대하여 음료수 채우기
result=0

for i in range(N):
  for j in range(M):
    #현재 위치에서 DFS 실행
    if dfs(i,j)==True:
      result+=1

print(result)#정답 출력