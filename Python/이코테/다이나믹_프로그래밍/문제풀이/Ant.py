#개미전사
#인접한 식량창고는 선택할 수 없음
#나의 풀이
'''
import sys;p=sys.stdin.readline
n=int(p().rstrip())
k=list(map(int,p().split()))
d=[0]*n
d[0]=k[0]
d[1]=k[1]
for i in range(2,n):
    d[i]=d[i-2]+k[i]
print(max(d[-2],d[-1]))
'''
#나동빈님 풀이
#정수 N을 입력
n=int(input())
#모든 식량 정보 입력받기
array=list(map(int,input().split()))

#앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d=[0]*100
#다이나믹 프로그래밍 진행(보텀업)
d[0]=array[0]
d[1]=max(array[0],array[1])
for i in range(2,n):
    d[i]=max(d[i-1],d[i-2]+array[i])
#결과 출력    
print(d[n-1])