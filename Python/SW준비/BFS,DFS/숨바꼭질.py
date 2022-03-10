import sys; input=sys.stdin.readline
from collections import deque
MAX=10**5
n,k=map(int,input().split())
graph=[0 for i in range(MAX+1)]
def bfs():
    q=deque()
    q.append(n)
    while q:
        x=q.popleft()
        #만약 동생을 만난다면, 해당 위치의 값을 반환 
        if x == k:
            return graph[x]
        for nx in [x-1,x+1,x*2]:
            #범위 내에 있고, 현재 위치에 방문한 적이 없는 경우 
            if 0<=nx<= MAX and graph[nx]==0:
                graph[nx]=graph[x]+1 #해당 위치의 값을 1 증가 시킴
                q.append(nx) #다음 추적을 위해 현재 좌표를 큐에 삽입 
value=bfs()                
print(graph[k:n+1])
            
