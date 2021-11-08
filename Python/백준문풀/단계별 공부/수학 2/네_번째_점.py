import sys;input=sys.stdin.readline
x=[]
y=[]
for i in range(3):
    a,b=map(int,input().split())
    try:
        x.index(a)
        x.remove(a)
    except:
        x.append(a)
    try:
        y.index(b)
        y.remove(b)
    except: 
        y.append(b)
print(*x,*y)


