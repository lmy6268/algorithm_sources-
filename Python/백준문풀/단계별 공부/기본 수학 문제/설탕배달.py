#BOJ2839
import sys; input=sys.stdin.readline
dp=[5001]*5001
dp[3]=1
dp[5]=1
n=int(input())
for i in range(6,n+1):
    if dp[i-3]!=5001:
        dp[i]=dp[i-3]+1
    if dp[i-5]!=5001:
        dp[i]=min(dp[i-5]+1,dp[i])
if dp[n]==5001:
    print(-1)
else:
    print(dp[n])




