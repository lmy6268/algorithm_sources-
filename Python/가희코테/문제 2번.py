#키워드 문제
import sys; p=sys.stdin.readline
n,m= map(int,p().rstrip().split()) #n:키워드 개수, m: 쓴 글의 개수 
k=dict() #dict 자료형을 이용하여 입력을 받음
cnt=n #잔여 키워드의 갯수를 체크하는 변수
res="" #결과 값을 저장
for i in range(n): 
    k[p().rstrip()]=False #입력한 값의 bool 값을 False로 초기화
for i in range(m):
    d=p().rstrip().split(',') #입력한 글을 리스트로 만듦
    for j in d: 
        if k.get(j)==False: #만약 j키가 있는 경우 
            k[j]=True
            cnt-=1
    res+=f"{cnt}\n"
print(res)

