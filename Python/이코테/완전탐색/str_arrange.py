#문자열 재정렬

# #내 코드
# inputData= list(input())
# sum=0
# result=[]
# for i in inputData:
#   if ord(i)>=ord('A') and ord(i)<=ord('Z'): #만약 i가 문자라면
#     result.append(i)
#   else: #숫자라면
#     sum+=int(i)
# result.sort()
# result=  "".join(result)
# if sum!=0:
#   result+=str(sum)
# print(result)

#나동빈님 코드
data =input()
result= [] #문자만 담는 리스트
value=0 #숫자값의 합을 위한 변수

#문자를 하나씩 확인하며
for x in data:
  #알파벳인 경우 결과 리스트에 삽입
  if x.isalpha():
    result.append(x)
  #숫자는 따로 더하기
  else: 
    value+=int(x)
#알파벳을 오름차순으로 정렬
result.sort()

#숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value!=0:
  result.append(str(value))
#최종 결과 출력(리스트르 문자열로 변환하여 출력)
print(''.join(result))