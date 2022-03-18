# import sys;input=sys.stdin.readline
# def binary_search(arr,target,st,en):
#     if st>en: #시작점이 끝점 인덱스보다 크다면, 이는 해당하는 값이 리스트에 없음을 의미
#         return 0
#     mid = (st+en)//2 
#     if arr[mid]==target:
#         return 1
#     if arr[mid]>target:
#         return binary_search(arr, target, st, mid-1)
#     else:
#         return binary_search(arr, target, mid+1, en)
# n=int(input())
# arr=list(map(int,input().split()))
# arr.sort()
# m=int(input())
# b=list(map(int,input().split()))
# for i in range(m):
#     print(binary_search(arr, b[i], 0, n-1),end=" ")
import sys;input=sys.stdin.readline
a,b,v=map(int,input().split())
if (v-a)%(a-b)==0:
    print(v//(a-b)-1)
else: print(v//(a-b)+1)

