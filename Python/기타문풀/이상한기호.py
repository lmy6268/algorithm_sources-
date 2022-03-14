import sys;input=sys.stdin.readline
def atFunc(a,b):
    return (a+b)*(a-b)
a,b=map(int,input().split())

print(atFunc(a, b))