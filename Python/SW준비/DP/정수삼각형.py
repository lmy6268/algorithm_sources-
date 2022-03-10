import sys;input=sys.stdin.readline
n=int(input())
graph=[]
graph.append([int(input())])
for i in range(1,n):
    a=list(map(int,input().split()))
    for j in range(len(a)):
        #입력값 중 인덱스가 0이거나 가장 마지막 자리인 경우, 이전단계에서의 max를 구하는 방법이 다름.
        if j==len(a)-1:
            a[j]=graph[i-1][j-1]+a[j]
        elif j==0:
            a[j]=graph[i-1][j]+a[j]
        else:
            a[j]=max(graph[i-1][j],graph[i-1][j-1])+a[j]
    graph.append(a)
print(max(graph[n-1]))