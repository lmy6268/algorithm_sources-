import sys;input=sys.stdin.readline
from itertools import permutations
n=int(input())
cnt=[0]*4 #모양 별 갯수
tmp=list(map(int,input().split()))
for i in tmp:
    num=i
    cnt[num]+=1
orders=[1,2,3]
orders=list(map(list,permutations(orders)))
res=987654321#최종 출력할 최소횟수 / 매 order를 거듭하면서 업데이트 된다.
for p in orders:
    sp=0 #영역을 넘기는 space역할 
    arr=[[0]*4 for i in range(4)]
    for i in range(3): #영역 별 갯수를 구한다.
        for j in range(cnt[p[i]]):
            #p[i]영역의 갯수만큼 루프/ 이부분에서 트릭=> tmp리스트의 p[i]영역(tmp[sp+j])에서 1~3모양이 각각 몇 개 있는지 확인
            arr[p[i]][tmp[sp+j]]+=1
        sp+=cnt[p[i]] #스페이싱 간격 +
    #첫번째 바구니에서 2,3번 모양의 갯수= 횟수이고, 
    #그 이후의 최소횟수는 2번 바구니에서 3번 모양의 갯수와 3번 바구니에서 2번 모양의 갯수중 
    #최댓값이 횟수가 되어
    #두 횟수를 합한 값이 이번 순열에서의 최소횟수가 된다. 
    #누적되어있는 최소횟수와 현재 구한 최소횟수중 더 작은 값을 결과값으로 저장한다. 
    res=min(res,arr[1][2]+arr[1][3]+max(arr[2][3],arr[3][2]))
    print(cnt,res,arr)
print(res)
