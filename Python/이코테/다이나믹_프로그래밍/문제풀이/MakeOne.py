#1로 만들기
#나동빈님 코드
import sys; p=sys.stdin.readline
n=int(p().rstrip())
#DP테이블 초기화(최대 30000까지 입력받을 수 있다고 했으므로)
d=[0]*30001
#다이나믹 프로그래밍 진행(보텀업)
for i in range(2,n+1):
    #현재의 수에서 1을 빼는 경우
    d[i]=d[i-1]+1
    #저장되어있는 값과 비교 했을 때 더 작은 값을 dp에 저장한다.
    if i%2==0:
        d[i]=min(d[i],d[i//2]+1)
    if i%3==0:
        d[i]=min(d[i],d[i//3]+1)
    if i%5==0:
        d[i]=min(d[i],d[i//5]+1)
print(d[n])