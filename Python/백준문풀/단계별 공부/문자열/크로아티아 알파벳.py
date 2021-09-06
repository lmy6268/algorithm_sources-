#BOJ2941
import sys;input=sys.stdin.readline
CA=["c=","c-","dz=","d-","lj","nj","s=","z="]
word=input().rstrip()
for i in CA:
    word=word.replace(i,"a")
print(len(word))