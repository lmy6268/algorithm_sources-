# import sys;input=sys.stdin.readline
# arr = [False, False, True] + [True, False] * 5000
# for number in range(3, 101, 2):
#     if arr[number]:
#         arr[number*2::number] = [False] * len(arr[number*2::number])

# for _ in range(int(input())):
#     k=int(input())
#     mid=int(k/2)
#     if arr[mid]:
#         print(mid,mid)
#     else:
#         for i in range(mid,2,-1):
#             if arr[i] and arr[k-i]:
#                 print(i,k-i)
#                 break
x = list(range(101))
print(x[10::6])