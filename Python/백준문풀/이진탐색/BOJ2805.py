
# st=0;en=max(arr) #시작값과 끝값을 지정함
# res=0 #설정할 수 있는 높이의 최댓값
# while st<=en:
#     total=0
#     b_b=False
#     mid=(st+en)//2 #현재 설정한 높이
#     #수정해야할 부분
#     for i in arr:
#         if i>mid:
#             total+=i-mid
#         if total>=m:
#             res=mid
#             st=mid+1
#             b_b=True
#             break
#     #여기까지
#     if not b_b:
#         en=mid-1
# print(res)    
'''답보고 나서 개선'''
import sys;p=sys.stdin.readline
from collections import Counter
n,m=map(int,p().rstrip().split()) #n 나무의 수, m 상근이가 집으로 가져가려고 하는 나무의 길이
woods=Counter(map(int,p().split())).items()
st,en= 0,max(woods)[0] #0 - max 값 범위에서 mid를 계산
res=0
while st<=en: #앞뒤가 역전되려는 순간 종료.
    mid = (st+en)//2  #중간값 
    total=0 
    for wood,c in woods:
        if wood>mid:
            total+=(wood-mid)*c
        if total>=m:
            res=mid
            st=mid+1
    else:
        en=mid-1
print(res)
