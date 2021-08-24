#효율적인 화폐구성
import sys;p=sys.stdin.readline
n,m=map(int,p().split())#n: 화폐의 가지 수, m: 가치의 합
cur=[int(p().rstrip()) for i in range(n)] #화폐를 담은 리스트
d=[0]+[10001]*m 
for c in cur:
    for i in range(c,m+1):
        if d[i-c]!=10001:
            d[i]=min(d[i],d[i-c]+1)
if d[m]!=10001:
    print(d[m])
else:
    print(-1)       
