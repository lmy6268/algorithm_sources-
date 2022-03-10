# import sys;input=sys.stdin.readline
# n=int(input()) #집의 수 
# color=4 #초기화 
# cost=[0 for i in range(n+1)]



# for i in range(1,n+1):
#     costs=list(map(int,input().split()))
#     if i!=1:
#         costs[color]=1001
#     tmp=1001
#     for j in range(3):
#         if tmp>costs[j]:
#             tmp=costs[j]
#             color=j
#     cost[i]=cost[i-1]+tmp
#     print(color,tmp)
# print(cost[n])

import sys;input=sys.stdin.readline
n=int(input()) #집의 수 
cost=[list(map(int,input().split())) for _ in range(n)]
for i in range(1,n):
    cost[i][0]=min(cost[i-1][1],cost[i-1][2])+cost[i][0]
    cost[i][1]=min(cost[i-1][0],cost[i-1][2])+cost[i][1]
    cost[i][2]=min(cost[i-1][0],cost[i-1][1])+cost[i][2]
print(min(cost[n-1][0],cost[n-1][1],cost[n-1][2]))

