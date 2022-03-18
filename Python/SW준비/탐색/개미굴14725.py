
### 틀렸습니다 코드 ###
import sys;input=sys.stdin.readline
from functools import cmp_to_key
n=int(input()) #로봇개미가 알게 된 먹이의 정보 개수 
info={} #로봇개미가 얻은 데이터 목록 

#각 노드 객체의 정보 
class Node:
    def __init__(self):
        floor=0
        root=""
    def dataIn(self,floor,food):
        self.floor=floor
        self.food=food
    def getFloor(self):
        return self.floor
    def getFood(self):
        return self.food
    def __str__(self):
        return f"{'--'*(self.floor)}{self.food}"


#객체의 크기 비교(정렬을 위함)
def sorting(x,y):
    if x.getFloor()==y.getFloor():
        if x.getFood()>y.getFood(): 
            return 1
        elif x.getFood()<y.getFood():
            return -1
        else:
            return 0
    return 0

#객체의 데이터 값이 같은지 비교
def check(x,y):
    if x.getFloor()==y.getFloor() and x.getFood()==y.getFood():
        return True
    else:
        return False

#데이터 입력 
for i in range(n):
    IN=input().rstrip().split()
    m=int(IN[0]); #로봇 개미 한 마리가 보내준 먹이 정보
    key=IN[1];food=IN[2:] #키: 루트노드 , 푸드: 각 층을 내려오면서 얻은 정보 
    if key not in info:
        info[key]=[]
    for t in range(m-1):
        node=Node()
        node.dataIn(t+1,food[t])
        flag=False
        for k in info[key]:
            if check(k,node):
                flag=True
                break
        if not flag:
            info[key].append(node)
#정렬 후 출력 
for i in sorted(info):
    print(i)
    t=sorted(info[i],key=cmp_to_key(sorting))
    for k in t:
        print(k)

    


# for i in range(n):
#     IN=input().rstrip().split()
#     m=int(IN[0]); #로봇 개미 한 마리가 보내준 먹이 정보
#     key=IN[1];food=IN[2:] #키: 루트노드 , 푸드: 각 층을 내려오면서 얻은 정보 
#     if  key  not in info:
#         info[key]=[]
#         for i in range(m-1):
#             info[key].append([food[i]])
#     else:
#         print(info[key],food,m-1,len(info[key]))
#         if m-1>len(info[key]):
#             info[key].extend([[]for i in range(m-1-len(info[key]))]) #배열의 길이가 부족한 만큼만 늘려줌
#             for i in range(m-1):
#                 info[key][i].append(food[i]) #먹이 정보를 삽입 
            
#         else:
#             for i in range(m-1):
#                 info[key].append([food[i]]) #먹이 정보를 삽입 
# for i in info:
#     print(i,info[i])
# for i in sorted(info): #루트 노드 사전순으로 정렬 
#     print(i) #루트노드 출력 
#     i=info[i]
#     for j in range(len(i)):
#         i[j].sort()
#         for k in range(len(i[j])):
#             print("--"*(j+1),end=" ")
#             print(i[j][k])
        


