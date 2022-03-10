# import sys;input=sys.stdin.readline
from collections import deque
n,m,k,x=map(int,input().split())
graph=[[] for _ in range(n)]
cost=[0  for _ in range(n)]

#방문리스트 
visited=[False for _ in range(n)]

#데이터 삽입 
for i in range(m):
    a,b=map(int,input().split())
    graph[a-1].append(b)#좌표가 1부터 시작해서 

def bfs(v):    
   
    q=deque()
    q.append(v)
    while q:
        a=q.popleft()
    #인접행렬에서 값을 꺼냄 
        for c in graph[a-1]:
            #방문하지 않았고, 시작점이 아닌 경우에만 큐에 추가 
            if visited[c-1]==False and c!=v:
                q.append(c)
                #인접 노드의 비용을 기준 노드의 값 +1 로 설정함. 
                cost[c-1]=cost[a-1]+1
                #인접 노드를 방문 처리 
                visited[c-1]=True
    result=sorted([i+1 for i in range(n) if cost[i]==k])
    return result
A=bfs(x)
if A!=[]:
    for i in A:
        print(i)
else:
    print(-1)

            
