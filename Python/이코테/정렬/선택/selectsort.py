
def selectSort(arr): #선택정렬
    n=len(arr)
    for i in range(n): #O(N)
        min_index=i
        #오름차순 정렬
        for j in range(i+1,n): #O(N)
            if arr[min_index]>arr[j]:
                min_index=j
        #내림차순 정렬
        '''
        for j in range(i+1,n):
            if arr[min_index]<arr[j]:
                min_index=j#범위 내에서 가장 큰 값을 계속해서 앞으로 끄집어냄 
        '''
        arr[i],arr[min_index]=arr[min_index],arr[i] #O(1)
    #시간 복잡도 : O(N)*O(N)= O(N^2)
    return arr
#입력한 데이터 
arr=[7,3,2,0,1,4,9,6,5,8]
#정렬 실행
print(selectSort(arr))