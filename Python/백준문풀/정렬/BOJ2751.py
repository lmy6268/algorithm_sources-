# import sys;p=sys.stdin.readline
# def quickSort(arr):
#     if len(arr)<=1:
#         return arr
#     pivot=arr[0]
#     tail=arr[1:]
#     left=[x for x in tail if x<=pivot]
#     right=[x for x in tail if x>pivot]
#     return quickSort(left)+[pivot]+quickSort(right)
import sys;p=sys.stdin.readline
n=int(p().rstrip())
arr=[int(p().rstrip())  for _ in range(n)]
arr.sort()
for i in range(n):
    print(arr[i])
