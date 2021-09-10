#BOJ1193
import sys;input=sys.stdin.readline
x=int(input())
line=1
top=0;down=0
while x>line:
    x-=line
    line+=1
    #사선라인이 짝수 번째일 경우
if line%2!=0:
    top=line-x+1
    down=x
else: #사선라인이 홀수 번째일 경우
    top=x
    down=line-x+1
print(f"{top}/{down}")
