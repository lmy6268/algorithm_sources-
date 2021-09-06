import sys;input=sys.stdin.readline
res=0
for i in range(int(input())):
    word=input().rstrip()
    tmp=''
    check=False
    for i in range(len(word)):
        if tmp=='':
            tmp=word[i]
        elif tmp!=word[i]: #만약에 연속된 문자가 아닌 다른 문자가 등장하는 경우
            if word[i+1:].count(tmp)>0: #연속된 문자가 이후에 또 등장한다면
                check=True
                break
            else: tmp=word[i]#아니라면 연속된 문자를 저장하는 변수를 새로이 등장하는 문자로 업데이트
    if check==False: #만약 그룹단어라면
        res+=1 #결과값을 1증가
print(res)