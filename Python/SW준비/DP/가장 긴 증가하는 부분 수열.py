import sys;input=sys.stdin.readline
def binarySearch(left,right,target):
    while left<right:
        mid = (left+right)//2
        if dp[mid]<target: #찾는 중간 값이 목적 값보다 작은 경우
            left= mid+1 #하한선을 1 올린다
        else:
            right=mid #아닌경우 상한선을 중간값으로 둔다
    return right

n=int(input())
arr=list(map(int,input().split()))
dp=[0 for i in range(n+1)]
dp[0]=arr[0]
i=1 ; j=0
while i<n:
    #만약 현재 수열의 마지막 수보다, 들어온 값이 더 큰 경우
    if dp[j] < arr[i]:
        dp[j+1] = arr[i] 
        j+=1
    else:
        idx=binarySearch(0,j,arr[i])
        dp[idx]=arr[i]
    i+=1
print(j+1)
