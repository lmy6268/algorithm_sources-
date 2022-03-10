#1: 1, 2:2 #3: 3 .. 흐름 
import sys;input=sys.stdin.readline
n=int(input())
dp=[0,1,2,3]+[0]*(n-3)
for i in range(4,n+1):
    dp[i]=(dp[i-2]+dp[i-1])%10007
print(dp[n])