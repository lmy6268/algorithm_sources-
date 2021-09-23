#BOJ2775
#미리 계산해 두고 필요할 때만 꺼내다 쓰도록 함.
import sys; input=sys.stdin.readline
A=[[i for i in range(1,15)]]+[[] for i in range(14)]
for i in range(1,15):
    for j in range(14):
        A[i].append(sum(A[i-1][:j+1]))
for _ in range(int(input())):
    k=int(input())
    n=int(input())-1
    print(A[k][n])