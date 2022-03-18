# import sys;input=sys.stdin.readline
# T=int(input())
# arr=[list(map(int,input().split())) for i in range(T)]
# cnt=0
# for i in arr:
#     if i.count(1)>=2:
#         cnt+=1
# print(cnt)


# import sys;input=sys.stdin.readline
# letters=len(list(set(list(input().rstrip()))))
# if letters%2==0:
#     print("CHAT WITH HER!")
# else:
#     print("IGNORE HIM!")


# #Soldier and Bananas
# import sys;input=sys.stdin.readline
# k,n,w=map(int,input().split())
# for i in range(1,w+1):
#     n-=(k*i)
# if n>=0:
#     print(0)
# else:
#     print(abs(n))

# #Beautiful Year
# yr=int(input())
# idx=yr+1
# while(True):
#     if len(list(set(str(idx))))==4:
#         print(idx)
#         break
#     idx+=1

#Games
# from collections import deque
# import sys
# input = sys.stdin.readline
# n = int(input())
# teams = [tuple(map(int, input().split())) for _ in range(n)]

# ex=[]
# host=0
# cnt=0
# matches=0;idx=0
# while (True):
#     host=guest.popleft()
#     if host in ex:
#         break
#     for i in guest:
#         if host[0]==i[1]:
#             cnt+=1
#     ex.append(host)
#     guest.append(host)
#     matches+=1
# print(cnt)


#GAMES
# import sys
# input = sys.stdin.readline
# n = int(input())
# teams = [tuple(map(int, input().split())) for _ in range(n)]
# j = 0
# res=0
# for i in range(n):
#     j = 0
#     while j < n:
#         if teams[i][0] == teams[j][1]:
#             res += 1
#         if j == i-1 and i !=n-1:
#             j += 2
#         else :j+=1
# print(res)


# #16진수
# import sys;input=sys.stdin.readline
# h=[str(i) for i in range(10)]+[chr(i+64) for i in range(1,7)]
# A=input().rstrip()
# sum=0
# for i in range(len(A),0,-1):
#     sum+= h.index(A[len(A)-i]) * 16 **(i-1)
# print(sum)

import sys;input=sys.stdin.readline
a=int(input())
arr=[int(input()) for i in range(a)]
for i in range(a):
    res=[]
    for j in range(arr[i]-1,0,-1):
        for k in range(j-1,0,-1):
            if k+j==arr[i]:
                res.append(f"{k} {j}")
    print(f"Pairs for {arr[i]}:",", ".join(res),sep=" ")
# i=0
# while a!=0:
#     i+=1
    
#     res=""
#     a*=3
#     if a%2:
#         a=(a+1)//2
#         res="odd"
#     else:
#         a//=2
#         res="even"
#     a=(a*3)//9
#     print(f"{i}. {res} {a}")
#     a=int(input())

    