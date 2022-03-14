import sys;p=sys.stdin.readline
n,m=map(int,p().split())#n: 화폐의 가지 수, m: 가치의 합
cur=[int(p()) for i in range(n)] #화폐를 담은 리스트
dp=[1]+[0 for i in range(m)]
for c in cur:
    for i in range(c,m+1):
        dp[i]+=dp[i-c]
print(dp[m])