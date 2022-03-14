import sys; input =sys.stdin.readline
n=int(input())

dp=[[1 for i in range(10)]]+[[0 for i in range(10)] for i in range(n)]
for i in range(1,n+1):
    dp[i][0]=1
    for j in range(1,10):
        dp[i][j]=sum(dp[i-1][:j+1])%10007
print(dp[n][-1])
     