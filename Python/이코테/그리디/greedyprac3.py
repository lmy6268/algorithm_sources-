N=int(input()) #인원수
fear = [int(i) for i in (input().split(" "))] #공포도
fear.sort()#오름차순 정렬

result =0 #총 그룹의 수
count =0 #현재 그룹에 포함된 모험가의 수

for i in fear: 
  #공포도를 낮은 것 부터 하나씩 확인(오름차순으로 정렬되어있으므로) 
  count +=1 #현재 그룹에 해당 모험가를 포함시키기

  if count>=i : #현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
    result += 1 #총 그룹의 수 증가
    count = 0 #현재 그룹에 포함된 모험가의 수 초기화 

print(result)
