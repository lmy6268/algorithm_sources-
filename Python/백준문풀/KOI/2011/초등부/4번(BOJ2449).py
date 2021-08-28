#전부 탐색하기엔 버거운 문제, 분할 정복과 dp테이블을 잘 사용해서 풀어야 합니다.

import sys;p=sys.stdin.readline
n,k=map(int,p().split())
#전구 색 입력
bulb=list(map(int,p().split()))
arr=[0]
for x in bulb:
    if bulb: arr.append(x) if arr[-1]!=x else arr.append(x)
n=len(arr)-1
dp=[[-1]*(n+1) for i in range(n+1)]
def CD(left,right):
    MAX=987654321
    #만약 길이가 1이라면 바꾸는 최소 횟수는 0이므로 0을 리턴 
    if left==right:
        return 0
    #이전에 이미 left - right 사이의 최소횟수를 구해 놓았다면, 그대로 그 값을 반환 
    if dp[left][right]!=-1:
        return dp[left][right] 
    #값을 계산하기 전, dp값을 무한대로 설정 
    dp[left][right]=MAX
    #왼쪽 부터 오른쪽 끝까지 탐색 
    for i in range(left,right):
        #만약 가장 왼쪽에 있는 전구의 색과 현재 위치의 색이 다를 경우
        tmp = 1 if arr[left]!= arr[i+1] else 0
        dp[left][right]=min(dp[left][right],CD(left,i)+CD(i+1,right)+tmp)
    return dp[left][right]
print(CD(1,n))
# #같은 색깔의 전구들 끼리 하나의 그룹으로 묶어서 진행
# import sys
# input = sys.stdin.readline
# inf = 1000000007

# n, k = map(int, input().split())
# bulb = list(map(int, input().split()))
# my_bulb = []
# for x in bulb:
#     if my_bulb:
#         if my_bulb[-1] != x:
#             my_bulb.append(x)
#     else:
#         my_bulb.append(x)

# lmb = len(my_bulb)
# dp = [[0 for y in range(lmb)] for x in range(lmb)]

# for x in range(lmb): #x는 right와 같음
    
#     for y in range(x-1, -1, -1): #y는 left와 같음 
#         m = inf
#         for k in range(y, x): 
#             temp = dp[y][k] + dp[k+1][x]

#             if my_bulb[k] != my_bulb[x]:
#                 temp += 1

#             if m > temp:
#                 m = temp

#         dp[y][x] = m

# print(dp[0][-1])
# print(dp)
# print(my_bulb)