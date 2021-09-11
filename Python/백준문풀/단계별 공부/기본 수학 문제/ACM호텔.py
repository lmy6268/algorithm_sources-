import sys;input=sys.stdin.readline
for _ in range(int(input())):
    h,w,n=map(int,input().split())
    if h==1:
        print(h,n if n//h>=10 else '0'+str(n),sep="")
    elif n%h==0:
        print(h,n//h if n//h>=10 else'0'+str(n//h),sep="")
    else:
        print(n%h,n//h+1 if n//h>=9 else '0'+str(n//h+1),sep="" )