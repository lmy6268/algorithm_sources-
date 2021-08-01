#단지번호붙이기
import sys
number=1#단지번호(전역변수)
count=0
def dfs(x,y):
  #주어진 범위를 벗어나는 경우에는 즉시 종료
    if x<=-1 or x>=N or y<=-1 or y>=N:
        return False
  #현재 노드를 방문하지 않았다면
    if visited[x][y] == False:
        #해당 노드 방문 처리
        visited[x][y] == True
        graph[x][y]=number
        #현재 노드의 상,하,좌,우 노드들도 재귀를 통해 호출
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False
N =int(input()) #N: 세로 , 가로
visited=[[False]*N for _ in range(N)]
graph=[]
result=[]
for i in range(N):
  graph.append(list(map(int,input())))
print(visited)
for i in range(N):
  for j in range(N):  
    if dfs(i,j)==True: #탐색이 종료되었을 때
      number+=1
      result.append(count)
      count=0
for i in result:
    print(i)