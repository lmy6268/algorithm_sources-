import sys;input=sys.stdin.readline
n=int(input()) #민규가 구매하려고 하는 카드의 개수
p=list(map(int,input().split())) #각 카드팩의 가격
dp=[0 for i in range(n+1)] #각 카드의 개수별로 지불해야하는 금액의 최댓값을 담은 리스트
for i in range(1,n+1):
    if i<=len(p): #필요한 카드 개수가 현재 주어진 카드팩의 길이보다 작거나 같은 경우
        cnt=i
    else:#필요한 카드 개수가 현재 주어진 카드팩의 길이보다 큰 경우
        cnt=len(p) 
    for c in range(cnt): #주어진 카드팩 만큼 순회.
#현재 최대값과  (현재 카드 개수 - 순회중인 카드팩이 가진 카드 수)의 최대값+순회중인 카드팩의 가격) 중 최대값을 찾음
        dp[i]=max(dp[i],dp[i-(c+1)]+p[c])  
#최종 결과값 출력
print(dp[n]) 