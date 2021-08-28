from itertools import combinations
import sys;input=sys.stdin.readline
N=list(int(input())for i in range(9))
answer=0
for i in list(combinations(N, 7)):
    if sum(i)==100:
        answer=i
        break
for i in sorted(answer):
    print(i)