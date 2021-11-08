#T1
# import sys;input=sys.stdin.readline
# def star(matrix,x,y,n):
#     if n==1:
#         matrix[y][x]='*'
#         return
#     for i in range(3):
#         for j in range(3):
#             if i!=1 or j!=1:
#                 star(matrix,x+(int(n/3)*j),y+(int(n/3)*i),int(n/3))
# n=int(input())
# matrix=[[' ' for i in range(n)] for i in range(n)] #matrix배열을 초기화
# star(matrix,0,0,n)
# for i in matrix:
#     print("".join(i))

#T2
import sys;input=sys.stdin.readline
def star(n):
    if n==3: return ["***","* *","***"]
    x=star(n//3)
    y=list(zip(x,x,x))
    for i in range(len(y)):
        y[i]=''.join(y[i])
    z=list(zip(x,[' '*(n//3)]*(n//3),x))
    for i in range(len(z)):
        z[i]=''.join(z[i])
    return y+z+y
result=star(int(input()))
print('\n'.join(result))