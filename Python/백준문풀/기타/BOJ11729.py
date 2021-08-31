import sys;input=sys.stdin.readline;print=sys.stdout.write
#빠른 알고리즘 = > 캐싱을 이용하셨다..
def hanoi(lv,sp,ep):
    dp={}
    def innerHanoi(lv,sp,ep):
        if (lv,sp,ep) in dp:
            return dp[(lv,sp,ep)]
        else:
            if lv==1:
                returnStr= str(sp)+" "+str(ep)
            else:
                Tmp=next((x for x in [1,2,3] if (x!=ep and x!=sp)))
                returnStr= "\n".join(c for c in [innerHanoi(lv-1, sp, Tmp),str(sp)+" "+str(ep),innerHanoi(lv-1, Tmp, ep)])
                dp[(lv,sp,ep)]=returnStr
            return returnStr
    print(innerHanoi(lv, sp, ep))
n=int(input())
print(str(pow(2,n)-1)+"\n")
hanoi(n,1,3)
#기본 알고리즘 
# def hanoi(n,sp,ep,sub): 
#     if n==1:#원판이 한개만 있다면 이동만 하면 끝 
#         print(str(sp)+" "+str(ep)+'\n')
#         return
#     hanoi(n-1, sp, sub, ep) #시작 기둥에서 보조기둥으로 원판 이동
#     print(str(sp)+" "+str(ep)+'\n') #목적지에 가장 큰 원판 이동
#     hanoi(n-1,sub,ep,sp) #보조 기둥에서 목적지로 원판 이동 
# n=int(input())
# print(str(pow(2,n)-1)+"\n")
# hanoi(n,1,3,2)
