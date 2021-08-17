import sys;p=sys.stdin.readline
from bisect import bisect_left as left,bisect_right as right
n,m=map(int,p().rstrip().split())
h=list(map(int,p().rstrip().split()))
st=0
en=max(h)
#이진탐색 수행
res=0#출력할 최종값
while(st<=en): 
    total=0
    mid=(st+en)//2 #중간점
    #배열 내의 값만 이용하는 거라 별도의 정렬이 필요 없음.!!
    for x in h:
        if x> mid:
            total+=x-mid
    #자른 떡의 양이 모자라는 경우 더 많이 자름(왼쪽 부분 탐색)
    if total<m: 
        en=mid-1
    #떡의 양이 충분한 경우 덜자르기 (오른쪽 부분 탐색)
    else:
        res=mid #중간값을 결과값에 저장
        st=mid+1 
print(res)