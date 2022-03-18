import sys;input=sys.stdin.readline
def bi_search(array,target,start,end): #배열,찾는 값,시작점,끝점
    if start>end:
        return 0
    mid=(start+end)//2 
    #target값을 찾은 경우 mid 인덱스 반환
    if array[mid]==target:
        return 1
    #중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid]>target:
        return bi_search(array, target, start, mid-1)
    #중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return bi_search(array, target, mid+1, end)
n=int(input())
des=list(map(int,input().split()))
des.sort()
m=int(input())
src=list(map(int,input().split()))
for i in src:
    print(bi_search(des, i, 0, n-1))