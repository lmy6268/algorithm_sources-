# import sys;input=sys.stdin.readline
# n=int(input())
# dp=[[1,0],[1,2]]+[[0 for i in range(2)] for i in range(n-1)]
# for i in range(2,n+1):
#    dp[i][0]=sum(dp[i-1])#공백인 경우
#    dp[i][1]=2*(dp[i-1][0]+dp[i-1][1]//2) #좌우 
#    dp[i-1]=sum(dp[i-1])%9901
# print(sum(dp[n])%9901)
from sys import stdin as inp
x,y=1,3 #0,1 일때 값
for i in range(int(inp.readline())-1): #n까지 값을 구하려고 함.
    x,y=y,(2*y+x)%9901 # 2*dp[n-1]+dp[n-2] 점화식 적용 => 왜 이게 나오는 지 모름..
print(y)