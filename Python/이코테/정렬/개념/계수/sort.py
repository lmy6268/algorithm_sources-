#모든원소의 값이 0보다 크거나 같다고 가정
arr=[7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
MAX_VALUE=max(arr)+1
#모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화
cnt = [0]*(MAX_VALUE)

for i in range(len(arr)):
    cnt[arr[i]]+=1#각 데이터에 해당하는 인덱스의 값 증가
for i in range(MAX_VALUE):
    for j in range(cnt[i]):#리스트에 기록된 정렬정보 확인
        print(i,end=" ")# 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력
