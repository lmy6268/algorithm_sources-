#BOJ1003
import sys;input=sys.stdin.readline
for _ in range(int(input())):
    do=[0,1];dz=[1,0] #갯수로 생각하기!!
    num=int(input())
    for i in range(2,num+1):
        do.append(do[i-1]+do[i-2])
        dz.append(dz[i-1]+dz[i-2])
    print(dz[num],do[num])