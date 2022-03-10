import sys;input=sys.stdin.readline
dp=[0,1,2,4]+[0]*8
for i in range(4,12):
    dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
for i in range(int(input())):
    print(dp[int(input())])