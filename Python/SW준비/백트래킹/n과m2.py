#1. itertools사용 
# from itertools import combinations as com
# n,m=map(int,input().split())
# arr=[str(i) for i in range(1,n+1)]
# for i in com(arr,m):
#     print(" ".join(i))

#2. dfs사용 

# import sys;input=sys.stdin.readline
# n,m=map(int,input().split())
# arr=[i for i in range(1,m+1)] #기본 리스트 
# visited=[False for _ in range(n+1)] #방문 처리를 위한 리스트 
# res=[]
# def dfs(n,m,depth): #길이와 고르는 개수 , 깊이
#     global arr,visited
#     if depth==m: #깊이가 우리가 원하는 개수와 같은 경우
#         r=[]
#         for i in arr: #깊이 만큼 arr에서 꺼냄
#             r.append(i)
#         r.sort() #사전순서대로 정렬 
#         if r not in res: #만약에 이 값이 res리스트에 없을 때만 append
#             res.append(r)
#         return
#     #목표 깊이에 아직 도달하지 못한 경우 
#     for i in range(n):
#         if not visited[i]: #방문하지 않은 노드인 경우
#             visited[i]=True #방문처리 
#             arr[depth]=i+1 #현재 깊이와 같은 위치에 있는 값을 i+1로 변경 
#             dfs(n,m,depth+1) #깊이를 1증가 
#             visited[i]=False #다시 방문 할 수 있도록 함
            
# dfs(n,m,0) #루트노드는 깊이가 0이므로, 0부터 시작
# for i in res:
#     for k in i:
#         print(k,end=" ")
#     print()

#3. dfs 효율적

import sys;input=sys.stdin.readline
n,m=map(int,input().split())
arr=[str(i) for i in range(1,m+1)] #기본 리스트 
def dfs(at,depth):
    if depth==m:
        print(" ".join(arr))
        return
    for i in range(at,n):
        arr[depth]=str(i+1)
        dfs(i+1,depth+1) #오름차순을 위해, 현재값보다 1큰 숫자부터 dfs를 진행.
dfs(0,0)