import sys;input=sys.stdin.readline
N=int(input())
x=0
for i in range(max(1,N-54),N):
    M=sum([int(k) for k in str(i)])
    if N==i+M:
        x=i
        break
print(x)