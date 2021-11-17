import sys;input=sys.stdin.readline
x=[]
y=[]
for i in range(int(input())):
    a,b=map(int,input().split())
    x.append(a);y.append(b)
score=[]
for t1,t2 in zip(x,y):
    count=1
    for i,j in zip(x,y):
        if i==t1 and j==t2:
            continue
        if t1>=i or t2>=j:
            continue 
        count+=1
    score.append(count)
for i in score:
    print(i,end=" ")