import sys;input=sys.stdin.readline
n=int(input()) #길이 
dp=[0,1,2]
for i in range(3,n+1):
    dp.append((dp[i-1]+dp[i-2])%15746) #수가 너무 커지면, 배열의 값도 커져서, 메모리 초과가 나온다..!
print(dp[n])

