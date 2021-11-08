import sys;input=sys.stdin.readline
def fac(N):
    if N==1 or N==0:
        return 1
    else:
        return N*fac(N-1)
print(fac(int(input())))