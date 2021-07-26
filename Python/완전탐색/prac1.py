#시각 문제
#00시 00분 00초부터 N시 59분 59초까지의 모든 시각중에서 3이 하나라도 포함되는 모든 경우의 수를 구함.
#총 경우의 수: 24*60 *60 = 86400
H=int(input())
result=0
for h in range(H+1):
  for m in range(0,60):
    for s in range(0,60):
      if '3' in str(h) + str(m) + str(s) :
        result+=1
print(result)
  