import sys;input=sys.stdin.readline
a,b,c=map(int,input().split())
def pow(b):
    if b==0:
        return 1
    tmp=pow(int(b/2))
    tmp=(tmp*tmp)%c
    if (b%2)==0:
        return tmp
    return (a*tmp)%c
print(pow(b))