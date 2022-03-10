# #암호문복호화
# # n과 b가 입력값으로 주어짐
# #암호화 이루어지는 과정: (n * 'c' (암호화할 대상) + b) mod 26 => (n * 'g' +b) %26 = 's'
# #입력값은 암호된 문자열, 출력값은 복호화된 문자열. 
import math
import sys;input=sys.stdin.readline
alpha=[chr(97+i) for i in range(26)]
a,b=map(int,input().split())
# s='o'
# A=((alpha.index(s)*26+b)*a)%26+alpha.index(s)


# s=list(input().rstrip()) #암호문 
# k=0
# print("before: ")
# for i in range(len(s)):
#     idx=alpha.index(s[i])
#     k+=idx
#     print(s[i],idx,(a*idx+b), alpha[(a*idx+b)%26])
#     s[i]= alpha[(a*alpha.index(s[i])+b)%26]
# print("after: ")
# print(s)
# print(k)
# for i in range(len(s)):
#     idx=alpha.index(s[i])
print(math.gcd(alpha.index('g'),26))