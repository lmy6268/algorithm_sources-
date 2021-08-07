#퀵정렬 예시 
arr=[7,3,2,0,1,4,9,6,5,8]#주어진 데이터
''' 
#슬라이싱 사용 x(arr원본이 변경)
def quickSort(arr,st,en): #arr: 입력된 데이터 배열 / st:시작점 / en:끝점
    if st>=en: #원소가 1개인 경우(시작점 = 끝점) 종료
        return 
    pivot =st #피벗은 첫 번째 원소로
    left = st+1 #왼->오 방향으로 피벗보다 큰 데이터 찾기
    right= en #오->왼 방향으로 피벗보다 작은 데이터 찾기
    #분할 만들기 
    while (left<=right):
        #피벗보다 큰 데이터를 찾을 때 까지 반복
        while(left<=en and arr[left]<= arr[pivot]):
            left+=1
        #피벗보다 작은 데이터를 찾을 때 까지 반복 
        while(right>st and arr[right]>=arr[pivot]):
            right-=1
        if (left>right):#만약 범위가 엇갈린 경우라면 작은 데이터와 피벗을 교체한다.
            arr[pivot],arr[right]=arr[right],arr[pivot]#swap
        else:#엇갈리지 않은 경우에는 작은 데이터와 큰 데이터를 교체
            arr[left],arr[right]=arr[right],arr[left]
    #분할 이후 과정(재귀적으로 quicksort 수행)
    quickSort(arr, st, right-1) #값이 피벗보다 작은 그룹
    quickSort(arr, right+1,en) #값이 피벗보다 큰 그룹
'''
#슬라이싱 사용 o(arr원본이 변경되지 않고 정렬된 새로운 arr이 생성)
def quickSort(arr):
    #리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(arr)<=1:
        return arr
    pivot = arr[0] #피벗은 첫 번째 원소
    tail=arr[1:]#피벗을 제외한 리스트
    left=[x for x in tail if x<=pivot] #분할된 왼쪽 부분
    right=[x for x in tail if x> pivot] #분할된 오른쪽 부분
    #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행 후 전체 리스트 반환
    return quickSort(left)+[pivot]+quickSort(right)
# quickSort(arr,0,len(arr)-1)
arr=quickSort(arr)
print(arr)