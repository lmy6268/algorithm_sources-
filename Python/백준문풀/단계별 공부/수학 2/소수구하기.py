import sys;input=sys.stdin.readline
M=123456*2+1
arr=[False,False]+[True]*M
for i in range(2,M):
    if arr[i]:
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                arr[i]=False
                break

while True:
    n=int(input())
    cnt=0
    if n==0:
        break
    for i in range(n+1,2*n+1):
        if arr[i]:
            cnt+=1
    print(cnt)