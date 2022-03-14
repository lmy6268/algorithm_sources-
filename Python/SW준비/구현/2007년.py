import sys;input=sys.stdin.readline
#2007년 x월 y일이 무슨 요일인지 알려주는 프로그램
day=["SUN","MON","TUE","WED","THU","FRI","SAT"] #요일
month=[0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #포인트! 
x,y = map(int,input().split()) #월 일 
#내가 원하는 달 이전 까지의 요일을 모두 더한 후, 원하는 날의 값을 더함.
result=(sum(month[:x])+y)%7
print(day[result])
