import sys; input=sys.stdin.readline
for _ in range(int(input())):
    x,y=map(int,input().split())
    dis=y-x #앞뒤 행성간 거리
    close = int(dis**0.5) #거리의 제곱근을 구함
    step=close*2-1 #각 규칙의 길이(Step 수) = 거리의 제곱근 *2 - 1 
    r=dis-close**2 
    if r!=0: #
        step = step +1 if r<=close else step+2 
    print(step) 
