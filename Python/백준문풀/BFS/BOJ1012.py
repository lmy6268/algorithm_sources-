#유기농 배추
from collections import deque
#빠른 입력을 위한 함수 import(버퍼를 이용하여 입력받음) #함수로 담아 지속적으로 사용해야겠다.
import sys; p=sys.stdin.readline;
#방향벡터(상하좌우)
dx=[-1,1,0,0]
dy=[0,0,-1,1]
#갯수를 저장하는 배열
res=[]
def bfs(x,y):
    #방문처리
    graph[x][y]=0
    #queue에 추가
    queue=deque()
    #오류가 생기지 않도록 튜플로 append
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        #방향별로 bfs수행
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            #범위를 벗어나지 않은 상태에서 해당 노드를 방문하지 않은 경우
            if nx>=0 and nx<n and ny>=0 and ny<m and graph[nx][ny]==1:
                graph[nx][ny]=0
                queue.append((nx,ny))
case = int(p())#테스트 케이스의 개수
for i in range(case):
    cnt=0 #갯수를 저장하는 변수
    n,m,k=map(int,p().split())
    graph=[[0]*m for _ in range(n)]#0으로 그래프 초기화
    for _ in range(k):
        a,b = map(int,p().split())
        graph[a][b]=1
    for x in range(n):
        for y in range(m):
            if graph[x][y]==1: 
                bfs(x,y)
                cnt+=1
    res.append(cnt) 
#결과값 출력 
for i in res:
    print(i)        
