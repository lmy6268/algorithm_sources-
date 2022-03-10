import sys; input=sys.stdin.readline
N=int(input())
row = [0] * N #힌 줄에 하나의 퀸만 놓아야 하므로 일차원 배열으로도 해결이 가능 .

ans=0

def isCrossed(x):
    for i in range(x):
        #y좌표가 같거나, 대각선 상에 위치해 있을 때는 퀸을 두면 안됨. 
        if row[x]==row[i] or abs(row[x]-row[i])==abs(x-i):
            return False
    return True 


def n_queens(x):
    global ans
    if x==N:
        ans+=1
    
    else: 
        for i in range(N):
            row[x]=i #(x,i)에 퀸 놓기 
            #퀸끼리 서로 만나지 않는 상황일 경우에만 깊이를 1 늘려 탐색
            if isCrossed(x):
                n_queens(x+1)
n_queens(0)
print(ans)