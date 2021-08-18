'''1. 표준라이브러리 이용

import sys;p=sys.stdin.readline 
from bisect import bisect_left as left, bisect_right as right  
#O(logN)으로 설계하기 위해 라이브러리 사용
def countrange(arr,x): 
    l=left(arr, x) #첫 위치를 저장
    r=right(arr, x) #마지막 위치를 저장
    return r-l
n,x=map(int,p().rstrip().split())
arr=list(map(int, p().rstrip().split()))
res=countrange(arr, x)
if res!=0:
    print(res)
else:
    print(-1)
'''

'''2. 이진탐색 직접 구현'''
import sys;p=sys.stdin.readline
res=0
def left(arr,x,st,en): #lower_bound
    while st < en:
        mid = (st + en) // 2
        #만약 찾는 값이 현재 중간값보다 큰 경우, 오른쪽 탐색
        if arr[mid] < x:
            st = mid + 1
        #만약 찾는 값이 현재 중간값보다 작거나 같은 경우, 왼쪽 탐색    
        else:
            en = mid
    return mid
def right(arr,x,st,en):#upper_bound
    while st < en:
        mid = (st + en) // 2
        #만약 찾는 값이 현재 중간값보다 작은 경우, 왼쪽 탐색
        if x < arr[mid]:
            en = mid
        #만약 찾는 값이 현재 중간값보다 크거나 같은 경우, 오른쪽 탐색    
        else:
            st = mid + 1
    return mid
def count(arr,x,st,en):
    global res
    res=right(arr, x, st, en) - left(arr, x, st, en)
n,x=map(int,p().rstrip().split())
arr=list(map(int, p().rstrip().split()))
count(arr,x,0,n-1)
print(res)

           
