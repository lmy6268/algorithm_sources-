import sys;input=sys.stdin.readline
n=int(input())
mo=10**9
dp=[0,[0]+[1 for _ in range(9)]]+[[0 for _ in range(10)] for _ in range(n-1)]

for i in range(2,n+1):
    dp[i][0]=dp[i-1][1]
    dp[i][9]=dp[i-1][8]
    for j in range(1,9):
        dp[i][j]=(dp[i-1][j-1]+dp[i-1][j+1]) #길이가 늘어닐 때마다,이전 길이의 끝자리 값이 1차이가 나는 값들의 합을 구하면 됨.
print(sum(dp[n])%mo)