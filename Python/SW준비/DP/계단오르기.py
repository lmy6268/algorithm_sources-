import sys;input=sys.stdin.readline
N= int(input())
stair=[0]+[int(input()) for i in range(N)]+[0,0,0]
dp=[[0,0] for _ in range(N+3)]

if N<=3:
    for i in range(1,N):
        dp[i][0]=stair[i]
        dp[i][1]=dp[i-1][0]
    print(max(dp[N-1])+stair[N])

else:
    for i in range(1,N+1):
        if i==1:
            dp[i]=[stair[i],0]
        elif i==2:
            dp[i][0]=dp[i-1][0]+stair[i]
            dp[i][1]=max(dp[i-1])
        else:
            dp[i][0]=max(dp[i-2][1]+stair[i-1],dp[i-2][0])+stair[i] #현재 계단을 밟은 경우 
            dp[i][1]=dp[i-1][0] #밟지 않은 경우 
    print(dp[N][0]) #맨 마지막 계단은 무조건 밟아야 하므로,,!! ㅜㅜ


