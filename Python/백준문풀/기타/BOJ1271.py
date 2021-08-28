import sys
n,m = map(int,sys.stdin.readline().rstrip().split(" "))
print( n//m ,n%m ,sep="\n") #//로 나눌 경우 int형으로 반환
