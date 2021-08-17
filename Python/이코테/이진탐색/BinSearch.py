import sys;p=sys.stdin.readline
#재귀적으로 구현한 이진탐색
def bi_search(array,target,start,end): #배열,찾는 값,시작점,끝점
    if start>end:
        return None
    mid=(start+end)//2 
    #target값을 찾은 경우 mid 인덱스 반환
    if array[mid]==target:
        return mid
    #중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid]>target:
        return bi_search(array, target, start, mid-1)
    else:
        return bi_search(array, target, mid+1, end)
n,target=list(map(int,p().rstrip().split()))
#전체원소 입력받기
array=list(map(int,p().rstrip().split()))

result=bi_search(array, target, 0, n-1)
if result==None:
    print("원소가 존재하지 않습니다. ")
else:
    print(result+1)