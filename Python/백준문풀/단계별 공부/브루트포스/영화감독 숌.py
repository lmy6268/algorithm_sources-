# BOJ1436
import sys
input = sys.stdin.readline
def endNum(x):
    countSix= [0 for _ in range(10)]
    for i in range(10):
        if x % 10 == 6:
            countSix[i] = 1
        x =  x//10
    for i in range(1,9):
        if (countSix[i - 1] == 1 and countSix[i] == 1 and countSix[i + 1] == 1):
            return 1
    return 0

n = (int)(input().rstrip())
count = 0
result = 0
for i in range(1000000):
    if endNum(i) == 1:
        count += 1
    if n == count:
        result = i
        break
print(result)