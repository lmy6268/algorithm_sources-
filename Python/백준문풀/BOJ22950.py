#이진수 나눗셈
import sys;p=sys.stdin.readline
p()
m=int(p().rstrip(),2)#이진수
divisor=int("1"+("0"*int(p())),2) #k를 이진법으로 변경
print ("YES" if bin(m%divisor)=='0b0'else "NO")



