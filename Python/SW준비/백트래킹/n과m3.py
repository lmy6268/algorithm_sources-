#1. 중복 순열을 이용
# import sys;input=sys.stdin.readline
# from itertools import product as p
# n,m=map(int,input().split())
# for i in p([str(i) for i in range(1,n+1)],repeat=m):
#     print(" ".join(i))
#2. DFS를 이용
import sys;input=sys.stdin.readline
n,m=map(int,input().split())
arr=[i for i in range(1,m+1)]
def dfs(n,m,depth):
    global arr
    if depth==m:
        for i in arr:
            print(i,end=" ")
        print()
        return
    for i in range(n):
        arr[depth]=i+1 #현재 깊이와 같은 위치에 있는 값을 i+1로 변경 
        dfs(n,m,depth+1) #깊이를 1증가
dfs(n,m,0)
