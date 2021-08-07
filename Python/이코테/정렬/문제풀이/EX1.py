#계수정렬 이용
'''
def sort(arr,mode):
    MAX_VALUE=max(arr)+1
    cnt=[0]*MAX_VALUE
    for i in range(len(arr)):
        cnt[arr[i]]+=1
    idx=0
    if mode==True:#오름차순
        for i in range(MAX_VALUE):
            for j in range(cnt[i]):
                arr[idx]=i
                idx+=1 
    else:#내림차순
        for i in range(MAX_VALUE-1,-1,-1):
            for j in range(cnt[i]):
                arr[idx]=i
                idx+=1 
    return arr
'''    
import sys;p=sys.stdin.readline
n,k=map(int,p().split())
A=list(map(int,p().rstrip().split()))
B=list(map(int,p().rstrip().split()))
A.sort()#오름차순정렬
B.sort(reverse=True)#내림차순정렬
for i in range(k):
    if A[i] < B[i]:
        A[i],B[i]=B[i],A[i]
print(sum(A)) #배열 A의 모든 원소의 합을 출력 

