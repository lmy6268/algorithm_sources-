# import sys;p=sys.stdin.readline
#두개의 포인터를 이용 => 시간초과 판정
'''
n,k= map(int,p().split())
tmp=list(map(int,p().split()))
s=1
e=1#시작 포인터와 끝 포인터
S=1 #길이가 K가 되면 멈춤
M=sum(tmp[:k])
m=0 #매 슬라이드에서의 결과값을 저장
while s<=e:
    if S==k:
        m+=tmp[e]
        if M<m:
            M=m
        s+=1
        e=s
        S=1
        m=0
    elif e==n-1:
        if M<m:
            M=m
        print(M)
        break
    else:
        m+=tmp[e]
        S+=1
        e+=1
'''
import sys;p=sys.stdin.readline
#누적합이 처음에 계산된 SUM에서 앞 뒤 값만 변경됨을 알게된 후 다시 짠 알고리즘
#그리고 성공 / 120ms
n,k= map(int,p().split()) #온도측정한 날짜 수, 몇일 연속으로 누적합을 계산할 지
tmp=list(map(int,p().split())) #온도값
S=sum(tmp[:k]) #0-k까지의 누적합을 구하고 시작(key point)
res=S #기존 값과 비교하기 위한 중간 연산에 사용될 변수
for i in range(1,n-k+1):
    S=S-tmp[i-1]+tmp[i+k-1]
    print(i,S)
    if res<S:
        res=S
print(res) 
