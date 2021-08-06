#오름차순 정렬 기준
data=[7,5,9,0,3,1,6,2,4,8]
#선택정렬 알고리즘 기본
len_data=len(data)
for i in range(len_data):
    min_index=i #가장 작은 인덱스
    for j in range(i+1,len_data):
        if data[min_index]>data[j]: #만약 현재 데이터가 맨앞의 데이터보다 값이 작을 경우
            min_index=j 
    data[i], data[min_index] = data[min_index],data[i] #스왑
print(data)    
