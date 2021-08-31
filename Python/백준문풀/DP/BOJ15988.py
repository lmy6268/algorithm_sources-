import sys;input=sys.stdin.readline
s=""
dp=[0,1,2,4]+[0]*(1000001-4)
for i in range(4,1000001):
        dp[i]=(dp[i-1]+dp[i-2]+dp[i-3])%1000000009
for _ in range(int(input())):
    n=int(input())
    s+=f"{dp[n]}\n"
print(s)