import sys;p=sys.stdin.readline
n=int(p().rstrip())
arr=list(map(int,p().rstrip().split()))
arr.sort()
cnt=0
for i in range(n):
    cnt+=sum(arr[0:i+1])
print(cnt)
