#LIS 알고리즘을 처음 배웠다. 
# 병사 배치하기
# 최악의 경우에도 O(N^2) 시간 복잡도를 가짐.
import sys;p=sys.stdin.readline
n=int(p())
s=list(map(int,p().split()))
#순서를 뒤집어 '최장 증가 부분 수열' 문제로 전환 
s.reverse()
#모든 수의 부분 수열의 최소 길이는 1이므로 1로 dp테이블을 초기화
d=[1]*n
#가장 긴 증가하는 부분 수열(LIS)알고리즘 수행
for i in range(1,n):
    for j in range(i):
        if s[j]<s[i]:
            d[i]=max(d[i],d[j]+1)
print(n-max(d))
