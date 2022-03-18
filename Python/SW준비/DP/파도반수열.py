import sys;input=sys.stdin.readline
dp=[0,1,1,1]+[0 for _ in range(97)]
for _ in range(int(input())):
    n=int(input())
    for i in range(4,n+1):
        if dp[i]==0:
            dp[i]=dp[i-2]+dp[i-3]
    print(dp[n])
