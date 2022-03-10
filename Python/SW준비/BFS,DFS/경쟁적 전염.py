import sys;input=sys.stdin.readline
from collections import deque
N,K= map(int,input().split())
graph=[[0 for _ in range(N) ]for _ in range(N)]
dx=[0,0,-1,1]
dy=[-1,1,0,0]
S,X,Y=0,0,0


#시간 정보를 입력해야 하는 문제, 방문 여부는 해당 위치의 데이터값으로 확인이 가능했다. 
queue=deque()
#initialize 
for i in range(N+1):
    if i==N:
        S,X,Y=map(int,input().split())
    else:
        a=list(map(int,input().split()))
        for j in range(N):
            graph[i][j]=a[j]
            if a[j]!=0:
                queue.append((i,j,0,a[j]))
        
queue=deque(sorted(queue,key=lambda x: x[3]))

if S>0:
    while queue:
        #queue 에서 x,y,s값을 가져옴 
        a=queue.popleft()
        x,y,s=a[0],a[1],a[2]
        #만약 제한된 시간과 같은 경우 break 
        if s==S:
            break
       
        #상하좌우로 전염 
        for i in range(4):
            nx=x+dx[i];ny=y+dy[i]
            if nx>=0 and nx<N and ny>=0 and ny<N:
                #해당 칸에 바이러스가 없을 때에만 전염시킬 수 있음.
                if graph[nx][ny]==0:
                    #전염시킴 
                    graph[nx][ny]=graph[x][y]
                    queue.append((nx,ny,s+1,graph[x][y]))

print(graph[X-1][Y-1])
    