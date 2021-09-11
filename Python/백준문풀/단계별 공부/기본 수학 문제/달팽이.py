#BOJ2869
import sys;input=sys.stdin.readline
a,b,v=map(int,input().split())
res=1
v-=a 
if v>0: #첫 날의 낮에 오른 높이가 정상에 도달하지 못한 경우
    if a-b>v: #a-b가 남은 길이를 커버할 만큼 충분히 크다면 
        res+=1
    else: #a-b가 남은 길이를 커버할 만큼 충분히 크지 않다면 
        res+=(v//(a-b)) #커버할 수 있을 만큼 나눔 
        if v%(a-b)!=0: #그래도 나머지가 존재한다면 
            res+=1 #1을 증가시킴 
print(res)    