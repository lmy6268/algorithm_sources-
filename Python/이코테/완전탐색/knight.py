'''
# 왕실의 나이트 #
8*8 좌표평면 
열(y) => a-h
행(x) => 1-8
수평 => 2칸 수직 1칸
or 수직 =>2칸 수평 1칸
중요 ! 방향벡터 정의!
'''
import time
start_time=time.time()
#내 코드

loc=input() #말의 위치
#세로
result=0
dx=[2,2,-2,-2,1,-1,1,-1] #방향벡터
#가로
dy=[1,-1,1,-1,2,2,-2,-2]
for i in range(len(dx)):
  nx=int(loc[1])+dx[i]
  ny=ord(loc[0])+dy[i]
  if ny>= ord('a') and ny<=ord('h') and nx>= 1 and nx<=8:
    result+=1
print(result)

# #나동빈님 코드 

# #현재 나이트의 위치 입력받기 
# input_data=input()
# row=int(input_data[1])
# column=ord(input_data[0])-ord('a')+1

# #나이트가 이동할 수 있는 8가지 방향 정의
# steps=[(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]
# #8가지 방향에 대하여 각 위치로 이동이 가능한 지 확인
# result=0 #최종으로 출력할 값
# for step in steps:
#   #이동하고자 하는 위치 확인
#   next_row = row + step[0]
#   next_column = column + step[1]
#   #해당위치로 이동이 가능하다면 카운트 증가
#   if next_row >=1  and next_row <=8 and next_column >=1 and next_column <8:
#     result+=1
# print(result)


end_time=time.time()
print("시간: ",(end_time-start_time)/1000,"초")


