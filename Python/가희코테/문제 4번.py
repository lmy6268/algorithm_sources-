import sys;p=sys.stdin.readline
from collections import deque
def bfs(v):

start=map(int,p().rstrip().split(":"))
n=int(p().rstrip())
schedule=[]
graph=[]
for i in range(n):
    s,e,t=p().rstrip().split()
    schedule.append((s,e,t))
print(schedule)