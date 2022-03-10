import sys;input=sys.stdin.readline
n=int(input())
dp=[i for i in range(n+1)] #모든 칸에 인덱스에 해당하는 값을 저장한다.
for i in range(1,n+1):
    for j in range(1,i):
        if j*j>i: #기준값보다 제곱수가 크면 멈춤.(작은 수부터 채워나감)
            break
        if dp[i]>dp[i-j*j]+1: #만약 현재 기준값의 길이보다, j*j값을 더하지 않은 상태에서의 길이 1 늘린것의 값이 작다면
            dp[i]=dp[i-j*j]+1 #dp[i-j*j]에 j*j값을 더해줬기에, 길이는 1 증가함.
print(dp[n])
