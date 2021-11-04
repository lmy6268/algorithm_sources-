import sys;input=sys.stdin.readline
arr = [False, False, True] + [True, False] * 5000
for number in range(3, 101, 2):
    if arr[number]:
        arr[number*2::number] = [False] * len(arr[number*2::number])

for _ in range(int(input())):
    k=int(input())
    mid=int(k/2)
    if arr[mid]:
        print(mid,mid)
    else:
        for i in range(mid,2,-1):
            if arr[i] and arr[k-i]:
                print(i,k-i)
                break


# for i in range(2,len(arr)):
#     if arr[i]:
#         for j in range(2,int(i**0.5)+1):
#             if i%j==0:
#                 arr[i]=False