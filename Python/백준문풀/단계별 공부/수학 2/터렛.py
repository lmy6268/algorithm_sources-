#BOJ 1002 터렛
# 두 원의 교점을 가지고 푸는 문제

# 다음과 같은 케이스가 존재
# 각 원의 반지름의 길이를 r,R(단, r<=R로 가정) 이라고 하고 두 원의 중심 사이의 거리를 D라고 할 때
#(1) 교점이 X
# - 1)r+R<D 인 경우
# - 2)D=0이면서 r!=R인 경우
# - 3)r+R>D 이면서 R-r>D인 경우
#(2) 교점이 1개 존재
# - 1)r+R<D 이면서, R-r=D 인 경우(내접)
# - 2)R+r=D인 경우 
#(3) 교점이 2개 존재
# - R-r<D<R+r인 경우
#(4) 교점이 무수히 많을 경우
# - D=0이면서 r=R인 경우

import sys; input=sys.stdin.readline
for _ in range(int(input())):
    x,y,r,X,Y,R=map(int,input().split())
    D=((X-x)**2+(Y-y)**2)**0.5
    if D==0:
        if r==R: #case(4)
            print(-1) 
        else: #case(1)-2
            print(0) 
    elif D>r+R: #case(1)-1
        print(0) 
    elif D == R+r: #case(2)-2
        print(1) 
    elif D<r+R: 
        if abs(r-R)< D: #case (3) 
            print(2) 
        elif abs(r-R)>D: #case (1)-3
            print(0)
        else: #case (2)-1
            print(1)
