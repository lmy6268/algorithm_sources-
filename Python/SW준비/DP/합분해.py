import sys; input=sys.stdin.readline
n,k=map(int,input().split())
dp=[1]+[0 for i in range(n)] 
for i in range(1,n+1):
    dp[i]=dp[i-1]*(i+k-1)//i #중복 조합을 이용하여 풀이! 
print(dp[n]%1000000000)