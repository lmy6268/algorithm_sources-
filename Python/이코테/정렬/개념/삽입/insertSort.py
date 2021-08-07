#삽입정렬 기본 (내가 해결하지 못함 ㅜ) 
def insertSort(arr):
    n=len(arr)
    for i in range(1,n):
        for j in range(i,0,-1): # 인덱스 i부터 1까지 1씩 감소하며 반복하는 문법
            if arr[j]<arr[j-1]: #한 칸씩 왼쪽으로 이동 
                arr[j],arr[j-1] = arr[j-1],arr[j] #swap
            else:#만약 자신보다 작은 데이터를 만나는 경우, 해당위치에서  멈춤
                break
    return arr
arr=[7,3,2,0,1,4,9,6,5,8]
print(insertSort(arr))