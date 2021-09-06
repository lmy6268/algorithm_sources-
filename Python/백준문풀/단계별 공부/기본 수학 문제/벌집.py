#BOJ2292 
#계차수열 이용 풀이
import sys;input=sys.stdin.readline
n=int(input())
sum=0;l=1 #레이어는 1부터 시작하므로 1로 선언 후 시작
if n==1:print(1)
else:
    while n>=sum:#각 레이어 별 최솟값: L1-2,L2-8,L3-20,L4-38 ~
        l+=1
        sum=2+3*l*(l-1)
    print(l)