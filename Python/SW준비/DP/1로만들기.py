import sys;input=sys.stdin.readline
N=int(input())
#그리디한 방법이었다.. 
# dp=[N]+[ 0 for i in range(N)]
# for i in range(1,N+1):
#     a=1000000000
#     b=1000000000
#     c=1000000000
#     if(dp[i-1]%3==0):
#         a=dp[i-1]/3
#     if(dp[i-1]%2==0):
#         b=dp[i-1]/2
#     else:
#         c=dp[i-1]-1
#     dp[i]= int(min(a,b,c))
#     if(dp[i]==1):
#         print(i)
#         break
# print(dp)
#참고 : https:#blockdmask.tistory.com/254

#bottom up
#1을 뺴는 계산부터 시작해서 작은 계산을 통해 미리 dp[i]에 (최대)값을 메모이제이션을 합니다.
#2로 나누어 떨어지는지 3으로 나누어 떨어지는 경우에 앞에 계산한 dp[i/2]와 dp[i/3]과  현재의 dp[i]와 비교를 하여
#그 중 최소 값을 dp[i]에 다시 저장(메모이제이션)합니다.
#dp의 인덱스와 그 값은 숫자와 해당 숫자를 만들기 위한 최소의 횟수로 구성됨.
#ex) dp[2] => 2를 만들기 위한 최소의 횟수

#dp로 풀어보기(작은 문제부터 큰 문제로 이어지기)
dp=[0,0]+[0 for i in range(N)]
for i in range(2,N+1):
    dp[i]=dp[i-1]+1 # 규칙 3: 1 빼기
    if(i%2==0):
        dp[i]=min(dp[i],dp[i//2]+1) # 규칙 2: 2로 나눠질 경우 2로 나눔
    if(i%3==0):
        dp[i]=min(dp[i],dp[i//3]+1) # 규칙 1: 3로 나눠질 경우 3로 나눔

print(dp[N])
