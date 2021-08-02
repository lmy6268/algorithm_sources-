'''힌트 보고 푼 것'''
# #단지번호
# cnt=0
# apt=[]
# #DFS를 이용하여 체크  
# def dfs(x,y):
#     global cnt
#     if x<=-1 or x>=n or y<=-1 or y>=n:
#         return 
#     if graph[x][y]=='0':
#         return
#     if graph[x][y]=='1':
#         cnt+=1
#         graph[x][y]=len(apt)+1
#         dfs(x-1,y)
#         dfs(x,y-1)
#         dfs(x+1,y)
#         dfs(x,y+1)
    
# #가로,세로 길이
# n= int(input())
# #그래프
# graph=[list(input()) for i in range(n)]
# for i in range(n):
#     for j in range(n):
#         if graph[i][j]=='1':
#             cnt=0
#             dfs(i,j)
#             apt.append(cnt)
# apt.sort()
# print(len(apt))
# for i in apt:
#     print(i)
'''
풀이 2
어느 사람의 풀이 
using DFS
''' 
# cnt=0 #단지번호별  건물 개수 카운트
# apt=[] #단지번호별 건물 개수를 담은 리스트
# number=1 #단지 번호
# #상하좌우 방향 벡터
# dx=[-1,1,0,0]
# dy=[0,0,-1,1]
# #dfs 정의
# def dfs(x,y):
#     global cnt,number
#     if x<=-1 or x>=n or y<=-1 or y>=n or graph[x][y]=='0':
#         number+=1
#         return 
#     if graph[x][y]=='1':
#         cnt+=1
#         graph[x][y]=number
#         for i in range(4):
#             nx=x+dx[i]
#             ny=y+dy[i]
#             dfs(nx,ny)
# if __name__ =='__main__':
#     n=int(input()) #가로, 세로 길이
#     graph=[list(input()) for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if graph[i][j]=='1':
#                 cnt=0
#                 dfs(i,j)
#                 apt.append(cnt)
#     apt.sort()#단지수대로 오름차순 정렬
#     print(len(apt))#단지 갯수 출력
#     for i in range(number):
#         print(i)

'''풀이 3 using BFS'''
from collections import deque
apt=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(x,y):
    num=1
    graph[x][y]=0#방문 처리
    queuex=deque([x])
    queuey=deque([y])
    while queuex and queuey:
        px=queuex.popleft()
        py=queuey.popleft()
        for i in range(4):
            nx=px+dx[i]
            ny=py+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<n and graph[nx][ny]=='1':
                graph[nx][ny]=0#방문처리
                num+=1
                queuex.append(nx)
                queuey.append(ny)
    return num  

n= int(input())
graph=[list(input()) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j]=='1':
            cnt=bfs(i,j)
            apt.append(cnt)
apt.sort()
flag=len(apt)
print(flag)
for i in range(flag):
    print(apt[i])