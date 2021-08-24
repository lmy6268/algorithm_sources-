#단순 재귀 방식
#피보나치 수열
'''
def fibo(x):
    if x==1 or x==2:
        return 1
    return fibo(x-1)+fibo(x-2)
print(fibo(4))
'''
#다이나믹 프로그래밍
#1.피보나치 수열을 탑다운으로 구현
'''
#한 번 계산된 결과를 메모이제이션(Memoization)하기 위하여 리스트 초기화
DP=[0]*100 
#피보나치 함수를 재귀적으로 구현(탑다운 다이나믹 프로그래밍 방식)
def fibo(x):
    if x==1 or x==2:
        return 1
    #이미 계산한 적이 있는 문제라면 그대로 반환
    if DP[x]!=0:
        return DP[x]
    DP[x]=fibo(x-1)+fibo(x-2)
    return DP[x]
print(fibo(99))
'''
#2.피보나치 수열을 보텀업 방식으로 구현
#앞서 계산된 결과를 저장하기 위한 DP테이블 초기화
d=[0]*100
#첫번째 피보나치 수와 두번쨰 피보나치 수는 1
d[1]=1;d[2]=1
n=99
#피보나치 함수를 반복문으로 구현(보텀업 다이나믹 프로그래밍 방식)
for i in range(3,n+1):
    d[i]=d[i-1]+d[i-2] #점화식 기입
print(d[n])