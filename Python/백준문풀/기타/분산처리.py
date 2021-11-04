
#단순 하게 풀이한 것, 느림
# for _ in range(int(input())):
#     a,b=map(int,input().split())
#     num=a**b
#     if num%10==0:
#         print(10)
#     else:
#         print(num%10)
import sys;input=sys.stdin.readline
l=[[10],[],[2,4,8,6],[3,9,7,1],[4,6],[],[],[7,9,3,1],[8,4,2,6],[9,1]]
for _ in range(int(input())):
    f_a,b =map(int,input().split())
    a=f_a%10
    if a in [1,5,6]:
        print(a)
    else:
        print(l[a][b%len(l[a])-1])
