import sys;input=sys.stdin.readline
while True:
    l=list(map(int,input().split()))
    if l.count(0)==3:
        break
    else:
        M=max(l)
        l.remove(M)
        if M**2==l[0]**2+l[1]**2:
            print("right")
        else:
            print("wrong")