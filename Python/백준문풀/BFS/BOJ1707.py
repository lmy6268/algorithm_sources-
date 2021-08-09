#이분 그래프
import sys; p=sys.stdin.readline;
from collections import deque

def bfs(v,g,c,color):
    queue=deque()
    queue.append(v)
    c[v]=color
    while queue:
        v=queue.popleft()
        for i in g[v]:# 정점 v와 인접한 정점 i
            #방문하지 않은 정점인 경우
            if c[i]==0:
                queue.append(i) #큐에 넣음
                c[i]=c[v]*(-1) #정점 v와 인접한 정점은 반대의 색으로 칠함
            #인접한 점과 같은 색인 경우 
            elif c[i]==c[v]: 
                return True #True를 반환하여, 이분그래프가 아님을 확인
                
K=int(p().rstrip()) #테스트케이스의 개수
result=[]*K


for i in range(K):
    v,e=map(int,p().rstrip().split()) #정점의 개수: v, 간선의 개수:e
    graph=[[] for _ in range(v+1)] #정점의 번호는 1부터 시작하므로
    colors=[0 for _ in range(v+1)] #모든 정점의 색을 0으로 초기화 
    checkBin=False#이분 그래프인지 여부 확인 Boolean
    for j in range(e): 
        a,b=map(int,p().rstrip().split())
        graph[a].append(b)
        graph[b].append(a)
    for k in range(1,v+1): 
        if checkBin:
            break
        if colors[k]==0: #방문하지 않은 정점인 경우 
            checkBin=bfs(k,graph,colors,-1)
    result.append(checkBin)
for i in range(K): #테스트 케이스 loop
    if result[i]: #이분 그래프가 아닌 경우
        print("NO")
    else: #이분 그래프인 경우
        print("YES")

