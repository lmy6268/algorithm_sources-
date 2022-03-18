import sys;input=sys.stdin.readline
n,m=map(int,input().split())
arr=[str(i) for i in range(1,m+1)]
def dfs(at,depth):
    if depth==m:
        print(" ".join(arr))
        return
    #시작점을 부여한다..! ()
    for i in range(at,n):
        arr[depth]=str(i+1)
        dfs(i,depth+1) #중복+ 오름차순 = 비내림차순
dfs(0,0)