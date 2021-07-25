import time
start_time=time.time()


# #내가 코딩한 것
# N,K= map(int,input().split(" "))
# count=0
# while(N!=1):
#   if(N%K==0):
#     N/=K
#     count+=1
#   else:
#     N-=1
#     count+=1


#나동빈님이 코딩하신 것

N,K= map(int,input().split(" "))
count=0
while True:
  #N이 K로 나누어 떨어지는 수가 될 때 까지 빼기
  target=(N//K)*K #만약 N이 K로 나누어 떨어지지 않을 때, 가장 가까운 K를 찾아서 저장  
  count+=(N-target)
  N=target
  #N이 K보다 작을 때(더이상 K로 나눌 수 없을 경우) 반복문 탈출 
  if N<K:
    break;
  #K로 나누기
  count+=1
  N//=K
#마지막으로 남은 수에 대하여 1씩 빼기
count+=(N-1)
end_time=time.time()
print(count)
print("소요된 시간:",(end_time-start_time)/1000)

 