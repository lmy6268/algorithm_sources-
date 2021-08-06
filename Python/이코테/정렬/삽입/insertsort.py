#삽입정렬 기본
data=[7,5,9,0,3,1,6,2,4,8]

for i in range(len(data)): #O(n)
    for j in range(i,0,-1): 
        if data[j]<data[j-1]: #이전데이터가 현재 데이터보다 큰 경우 스왑.
            data[j],data[j-1] = data[j-1],data[j]
        else: #자신보다 작은 데이터를 만나는 경우엔 멈춤
            break 
print(data)