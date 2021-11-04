#BOJ 1085
import sys;input=sys.stdin.readline
x,y,w,h=map(int,input().split())
width=w-x;height=h-y
print(min(x,y,width,height))