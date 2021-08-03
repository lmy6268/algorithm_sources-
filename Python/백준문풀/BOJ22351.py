#수학은 체육과목 입니다
import sys;p=sys.stdin.readline
s=p().rstrip()
volume=1#배열의 칸수를 얼마나 차지하는지
i=0
result=[]

while True:
    length=(i+volume)#처음은 0+1=1/2+1=3/4  
    k=int(s[i:length]) #1차: s[0:1] /2차:s[2:3] / 3: s[2:4]
    if length>len(s)-1:
        # if len(result)==0:
        #     print("sda")
        #     print(s,s)
        # else:
        # print(result[0],result[-1:])
        break 
    cp=int(s[i+1:length+1])
    if cp==k+1:#s[1:2] 
        i=length#i=2
        result.append(k)#result=[s[0],]
    if cp<k+1:#s[3:4]==1 <10
        # i=length+1#i=2
        print(cp)
        volume+=1
        result.append(k)
    if cp==k:
        volume+=1
        

print(result)
    
    
