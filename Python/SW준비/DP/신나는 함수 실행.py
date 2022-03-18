import sys;input=sys.stdin.readline
sys.setrecursionlimit(10**7)

#코드 참고 :https://st-lab.tistory.com/190

# 첫번째 시도: 시간초과 난 코드 
# d={(0,0,0):1} #결과를 메모이제이션  
# def w(a,b,c):
#     if a*b*c<=0:
#         return d[(0,0,0)] #1을 리턴 
#     elif a>20 or b>20 or c>20: 
#         return d[(20,20,20)]
#     try:
#         return d[(a,b,c)]
#     except:
#         if a<b<c:
#             d[(a,b,c)]=w(a,b,c-1) + w(a, b-1, c-1) - w(a, b-1, c)
#             return d[(a,b,c)]
#         else:
#             d[(a,b,c)]= w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
#             return d[(a,b,c)]
        
# for i in range(21):
#     for j in range(21):
#         for k in range(21):
#             w(i,j,k)
# a,b,c=map(int, input().split())
# while True:
#     if (a,b,c)==(-1,-1,-1):
#         break
#     print(f"w({a}, {b}, {c}) = {w(a,b,c)}")
#     a,b,c=map(int, input().split())

#두 번째 시도: 웹에서 코드를 참고 
dp = [[[0]*(21) for _ in range(21)] for _ in range(21)] #삼차원 리스트로 각각의 값을 담는다..!
#최대 범위가 20까지이므로, 21까지만 리스트를 생성 
def w(a,b,c):
    #a,b,c 범위 조절
    if a<=0 or b<=0 or c<=0:
        return 1
    if a>20 or b>20 or c>20:
        return w(20,20,20)
    #만약 해당하는 값이 이미 저장되어있다면, 그 값을 반환 
    if dp[a][b][c]:
        return dp[a][b][c]
    #해당범위에 값이 일치하는 경우
    if a<b<c:
        #계산한 결과를 리스트에 메모이제이션한다. 
        dp[a][b][c]=w(a,b,c-1)+w(a,b-1,c-1)-w(a,b-1,c)
        #그 값을 반환 
        return dp[a][b][c]
    #위 if문에 걸리지 않은 경우
    dp[a][b][c]=w(a-1,b,c)+w(a-1,b-1,c)+w(a-1,b,c-1) - w(a-1,b-1,c-1)
    return dp[a][b][c]
a,b,c=map(int, input().split())
while True:
    if (a,b,c)==(-1,-1,-1):
        break
    print(f"w({a}, {b}, {c}) = {w(a,b,c)}")
    a,b,c=map(int, input().split())
    