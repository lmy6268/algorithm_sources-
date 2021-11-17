import sys;input=sys.stdin.readline
from itertools import combinations
N,M=map(int,input().split())
card=list(map(int,input().split()))
MAX=max(sum(i) for i in combinations(card,3) if sum(i)<=M)
print(MAX)