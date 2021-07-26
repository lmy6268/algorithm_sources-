##문제 : 곱하기 혹은 더하기 를 사용하여 최대값 만들기 

#시간 계산을 위한 초기값 생성 
import time
start_time=time.time()

# #내 코드 
# data = input()
# 
# data=[int(x) for x in data]
# result=0
# for i in data:
#   if i<=1 or result <=1 :
#     result+=i
#   else:
#     result*=i
# print(result)

#나동빈님 코드
data = input()
#첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1,len(data)):
  #두 수(입력값 혹은 현재 값) 중에서 하나라도 '0' 혹은 '1' 인 경우, 곱하기 보다는 더하기 수행 
  num =int(data[i])
  if num <=1 or result<=1:
    result+= num
  else:
    result *= num

#시간 계산 
print(result)
end_time=time.time()
print("소요된 시간:",(end_time-start_time)/1000,"초")