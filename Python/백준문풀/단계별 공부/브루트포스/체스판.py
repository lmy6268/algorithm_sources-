#다시 칠하기는 가능하지만 미리 주어진 판에 크기에 맞추어 자르기가 불가능

# import sys;input=sys.stdin.readline
# from collections import deque
# #UDLR
# dx=[1,-1,0,0]
# dy=[0,0,-1,1]
# chess=[]
# color=['W','B']
# count=[]
# def bfs(x,y):
#     count=0
#     visited[x][y]=True
#     queue=deque()
#     queue.append((x,y))
#     while queue:
#         px,py = queue.popleft()
#         idx=color.index(chess[px][py])
#         now=chess[px][py]
#         print(now,px,py)
#         for i in range(4):
#             nx=px+dx[i]
#             ny=py+dy[i]
#             if nx>=0 and nx<n and ny>=0 and ny<m and visited[nx][ny]==False:
#                 visited[nx][ny]=True
#                 if chess[nx][ny]==now:
#                     chess[nx][ny] = color[idx-1]
#                     count+=1
#                 queue.append((nx,ny))
#     return count
# n,m=map(int,input().split())
# for i in range(n):
#     chess.append(list(input().strip()))
    
# visited=[[False] * m for i in range(n)] 
# count.append(bfs(0,0))
# print(min(count))
import sys;input=sys.stdin.readline
def wbcnt(x,y):
    cnt=0
    for i in range(8):
        for j in range(8):
            if WB[i][j]!=board[x+i][y+j]:
                cnt+=1
    return cnt

def bwcnt(x,y):
    cnt=0
    for i in range(8):
        for j in range(8):
            if BW[i][j]!=board[x+i][y+j]:
                cnt+=1
    return cnt

W=list("WB"*4)
B=list("BW"*4)
cnt=-1
WB=[W if i%2 == 0 else B for i in range(8)]
BW=[B if i%2 == 0 else W for i in range(8)]
n,m=map(int,input().split())
board=[input().strip() for i in range(n)]
#최상단 좌측 좌표를 기준점으로 둔다
for i in range(n-7): #기준점을 위해 -7 하는 것이 포인트!(체스판의 크기가 8*8로 정해져 있으므로!) 
    for j in range(m-7):
        if cnt!=-1:
            #기준점에서 기존 체스판과 대조하여 그것과의 최소값을 구함
            cnt=min(cnt,wbcnt(i,j),bwcnt(i,j))
        else:
            cnt=min(wbcnt(i,j),bwcnt(i,j))
print(cnt)




