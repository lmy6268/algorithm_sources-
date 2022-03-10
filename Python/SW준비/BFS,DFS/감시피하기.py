from collections import deque
from itertools import combinations as combi
import sys
input = sys.stdin.readline
#initialize
N = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
graph = [[0 for i in range(N)]for _ in range(N)]
isEmpty = [] #빈공간의 좌표를 담음 (이후에 조합을 돌림.)
Teacher = [] #선생님의 좌표를 담는 리스트 
answer = False 

#insert data 
for i in range(N):
    a = input().rstrip().split()
    for j in range(N):
        if a[j] == 'X':
            isEmpty.append((i, j))
        elif a[j] == "T":
            Teacher.append((i, j))
        graph[i][j] = a[j]

#define bfs func
def bfs(tmp):
    for t in Teacher:
        for i in range(4):
            x,y=t
            #만약 범위내에 존재하고, 해당 칸에 장애물이 없는 경우
            while 0 <= x < N and 0 <= y < N and tmp[x][y] != "O":
                #학생이 발견된다면 false 리턴함
                if tmp[x][y] == "S":
                    return False
                x+=dx[i]
                y += dy[i]
    return True


#do combinations & brute-force
#비어있는 공간에 장애물을 두므로, 비어있는 공간에 3개의 데이터를 삽입함.
for i in combi(isEmpty, 3):
    #tmp리스트에 graph를 복사함.
    tmp = [item[:] for item in graph]
    for t in i:
        x, y = t
        tmp[x][y] = "O"
    if (bfs(tmp) == True):
        print("YES")
        answer = True
        break
if not answer:
    print("NO")
