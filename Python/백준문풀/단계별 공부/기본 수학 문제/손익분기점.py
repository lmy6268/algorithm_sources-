#BOJ1712
import sys;input=sys.stdin.readline
a,b,c=map(int,input().split())
print("-1") if b>=c else print(a//(c-b)+1)

    
