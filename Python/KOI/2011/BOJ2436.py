#다른 분의 질문 속 풀이
'''
import sys;input=sys.stdin.readline
from math import gcd
def findDivisor(n):
    global M
    num=n
    for i in range(1,int(num**0.5)+1):
        if num%i==0:
            j=int(num/i)
            if gcd(i,j)!=1:
                continue
            else:
                M=i

g,l=map(int,input().split())
M=1 #최대공약수
val=0
if g==l:
    print(g,l)
    sys.exit()
else:
    val=int(l/g) #구할 두 수의 곱과 값이 같음
findDivisor(val)
v=val / M 
print(M*g , int(v*g))
'''
import sys;input=sys.stdin.readline
from math import gcd
def G(a,b):return G(b,a%b) if b else a #최대공약수(유클리드 호제법)
a,b=map(int,input().split())
m,n=1,0 #m은 현재 나누는 값(약수를 구하기 위한 변수) 1부터 시작하지 않으면 아래에서 에러를 출력함(divide by zero), 최소공배수를 최대공약수로 나누면 최소공배수의 약수의 곱이 나옴 (b=a*x*y 이므로)
res1,res2=0,0
while m*m<=b//a: #최대공약수와 최소공배수가 같을 때도 고려. 
    n=b//a//m  
    if (b//a)%m: #나누어 떨어지는 경우 == m이 우리가 원하는 값의 약수일 경우  
        m+=1 
        continue
    if G(n,m)>1: #n,m이 서로소가 아닌지 확인
        m+=1
        continue
    if m*n == b//a: #m,n 곱이 최소공배수의 약수의 곱과 같은 경우
        res1,res2=m*a,n*a
    m+=1 
print(res1,res2)

'''나는 a의 배수를 다 나열한 후에, 그 안에서 이중 for문을 이용하여 답을 구하려고 만하다보니, 시간초과의 굴레에서 벗어나지 못하였는데, b//a는 생각을 못했다. 
해당 수가 서로소인지 아닌지, 체크하는 것도 몰랐고. 범위 지정 부터, 로직 설계까지 다 새롭다. 
'''