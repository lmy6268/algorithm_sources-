#바이러스 문제
from collections import deque
cnt=0
def bfs(v):
    global cnt
    queue=deque([v])
    visited[v]=True
    while queue:
        t=queue.popleft()
        cnt+=1
        for i in graph[t]:
            if visited[i]==False:
                queue.append(i)
                visited[i]=True
    cnt-=1 #1번컴퓨터는 제외
num = int(input())
cp = int(input())
graph=[[] for _ in range(num+1)]
visited=[False for _ in range(num+1)]
for i in range(cp):
    bn,an=map(int,input().split()) 
    graph[bn].append(an)
    graph[an].append(bn)
bfs(1)
print(cnt)
