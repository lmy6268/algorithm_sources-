#BOJ5622
import sys; input=sys.stdin.readline
dial=["","","ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
word=input().rstrip()
print(sum([i+1 for j in word for i in range(10) if j in dial[i]]))
