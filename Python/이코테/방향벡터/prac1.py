##상하좌우##

#문제 
'''N*N 공간에 서있는 여행자 A 
#1 : 가장 왼쪽위 좌표 (1,1), 가장 오른쪽 아래 좌표는 (N,N) /시작 좌표는 (1,1) 
#2 : 하나의 줄에 띄어쓰기 기준 => L,R,U,D 중 하나의 문자가 반복적으로 적혀있음. (단, 공간을 벗어나는 움직임은 무시.)
 L :왼쪽 한칸 이동 / R :오른쪽 한칸이동 / U: 위로 한칸이동 / D : 아래로 한칸 이동
#3 구하고자 하는 것 : 입력한 값에 도달하는 위치의 좌표
'''

#나의 코드

# N= int(input()) #공간의 크기
# M= input().split(" ") #이동하는 계획서 내용
# #RLDU
# dx=[0,0,1,-1] #행벡터
# dy=[1,-1,0,0] #열벡터 
# x,y=1,1#시작점
# for i in M:
#   if(i=='L'):
#     x+=dx[1]
#     y+=dy[1]
#     if x<1 or x>N or y<1 or y>N:
#       x-=dx[1]
#       y-=dy[1]    
#   if(i=='R'):
#     x+=dx[0]
#     y+=dy[0]
#     if x<1 or x>N or y<1 or y>N:
#       x-=dx[0]
#       y-=dy[0]
#   if(i=='U'):
#     x+=dx[3]
#     y+=dy[3]
#     if x<1 or x>N or y<1 or y>N:
#       x-=dx[3]
#       y-=dy[3]
#   if(i=='D'):
#     x+=dx[2]
#     y+=dy[2]
#     if x<1 or x>N or y<1 or y>N:
#       x-=dx[2]
#       y-=dy[2]
# print(x,y)

#동빈님의 코드

#N 입력 받기
N=int(input())
x,y =1,1 #초기 위치
plans =input().split() #기본값은 space를 기준으로 split

#L,R,U,D에 따른 방향벡터
dx=[0,0,-1,1]#행벡터
dy=[-1,1,0,0] #열벡터 
move_types=['L','R','U','D']

#이동계획 하나씩 확인
for plan in plans:
  #이동후 좌표 구하기
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx=x+dx[i]
      ny=y+dy[i]
    #공간을 벗어날 경우 제외
  if(nx<1 or ny<1 or nx>N or ny>N):
    continue; #무시함
    #이동을 수행
  x,y=nx,ny #이동한 값을 x,y에 대입
print(x,y)