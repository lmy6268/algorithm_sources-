#가희와 은행
from collections import deque
import sys;p=sys.stdin.readline
n,t,w= map(int, p().rstrip().split()) #n은 영업전에 온 대기자의 수, t: 한 고객당 처리하는 데 소요되는 시간 , w: 체크를 끝내는 시간(최종 출력의 루프 범위값)
res=""
time=0
queue=deque()
for i in range(n): #O(N)
    iD,T=map(int, p().rstrip().split())#id와 t=> 고객번호와 일을 처리하는데 소요되는 시간
    queue.append([iD,T])
m=int(p().rstrip())
temp=dict() #이후에 들어오는 사람들을 담는 dictionary
for i in range(m):#O(N)
    iD,T,C=map(int, p().rstrip().split())#iD,T,c =>id 는 고객 번호, T는 일을 처리하는데 소요되는 시간, c는 영업시작후 몇초뒤에 온 손님인지 
    temp[C]=[iD,T] 
a=queue.popleft()
for i in range(1,w+1): #O(N)
    res+=f"{a[0]}\n"
    a[1]-=1
    time+=1
    if temp.get(i)!=None: #만약에 영업시간 이후 i초 후 온 손님이 있다면
        queue.append(temp.pop(i)) #대기열에 손님 추가 
    if time==t or a[1]==0: #누적된 시간이 할당된 시간과 같거나, 손님이 일을 처리하는 시간이 다되었을 경우 
        time=0#누적하는 것을 초기화
        if a[1]!=0: #만약 여전히 시간이 필요한 손님인 경우 
            queue.append(a) #대기열 끝에 손님 추가 
        if i!=w:#제한된 시간과 i가 일치하지 않을 경우에만 pop을 실행함    
            a=queue.popleft()
print(res)