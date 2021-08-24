#Bottom_Up방식
#내 코드
'''
import sys;p=sys.stdin.readline
T=int(p())
res=[]
for t in range(T):
    n,m=map(int,p().split())
    #금광의 표를 그림 (한번에 담을 수 없으므로 tmp리스트를 활용하여 나눠담음)
    tmp=list(map(int,p().split()))
    dp=[]
    #dp테이블에 제시된 n,m 크기대로 리스트를 쪼개서 담음
    for i in range(0,n*m,m):
        dp.append(tmp[i:i+m])
    #최대값을 구함
    #가로 loop
    for i in range(1,m):
        #세로 loop
        for j in range(n):
            if j>0 and j<n-1: #이땐 위,가운데,아래 다 확인
                dp[j][i]=max(dp[j-1][i-1],dp[j][i-1],dp[j+1][i-1])+dp[j][i]
            if j==0: #이땐 가운데,아래만 확인
                dp[j][i]=max(dp[j][i-1],dp[j+1][i-1])+dp[j][i]
            if j==n-1: #이땐 위,가운데만 확인
                dp[j][i]=max(dp[j-1][i-1],dp[j][i-1])+dp[j][i]  
    #맨 마지막 위치에서 가장 많은 금을 출력              
    res.append(max([dp[i][m-1] for i in range(n)]))
for i in res:
    print(i)
'''
#나동빈님 코드
#테스트 케이스 입력
for tc in range(int(input())):
    #금광 정보 입력
    n,m=map(int,input().split())
    array=list(map(int,input().split()))
    #다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
    dp=[]
    #리스트 슬라이싱을 위한 index
    index=0
    for i in range(n):
        dp.append(array[index:index+m])
        index+=m
    #다이나믹 프로그래밍 진행
    for j in range(1,m):
        for i in range(n):
            #왼쪽 위에서 오는 경우
            if i==0: left_up=0
            else: left_down=dp[i-1][j-1]
            #왼쪽 아래에서 오는 경우
            if i==n-1:left_down=0
            else:left_down=dp[i+1][j-1]
            #왼쪽에서 오는 경우
            left=dp[i][j-1]
            dp[i][j]=dp[i][j]+max(left_up,left,left_down)
    result=0
    for i in range(n):
        result=max(result,dp[i][m-1])
    print(result)