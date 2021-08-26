import sys;input=sys.stdin.readline
n=int(input())
scale=list(map(int,input().split()))
scale.sort()
m=1#최솟값
for i in range(n):
    if m<scale[i]:
        break
    m+=scale[i]
print(m)


    