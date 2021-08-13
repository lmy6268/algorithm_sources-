# 정렬
import sys;r= sys.stdin.readline;
from functools import cmp_to_key
def cmp(x,y): #오름차순 기준 
    xf,xt=x.split('.'); yf,yt=y.split('.') #f: 파일명, t: 확장자명
    xused=ext.get(xt);yused=ext.get(yt) #가희 os에서 인식하는지 확인
    if xf>yf: 
        return 1
    elif xf==yf:
        if xused!=None and yused!=None:
            if xt>yt:
                return 1
            return -1
        elif xused!=None and yused==None:
            return -1
        elif xused==None and yused!=None:
            return 1
        else: #위 조건에 해당하지 않을 경우(둘다 가희 os에서 인식 못하는 경우)
            if xt>yt: 
                return 1
            return -1
    else:
        return -1
n, m = map(int, r().rstrip().split())  # n: 파일 개수 / m:확장자 개수
files =[]
ext = dict()
for i in range(n):
    files.append(r().rstrip())
for i in range(m):
    ext[r().rstrip()]=i
files.sort(key=cmp_to_key(cmp))
for i in files:
    print(i)
