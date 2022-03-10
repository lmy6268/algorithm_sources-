import sys;input = sys.stdin.readline

#체크하는 함수 
def check(value, tmp,answer):
    if value > 1:
        answer += f"{value}{tmp}"
    else:
        answer += f"{tmp}"
    return answer
def solution(s):
    best = 1001  # 길이가 짧은 경우의 길이 값을 가지는 변수 
    answer = ""
    if len(s)==1:
        return 1
    else:
        for k in range(1, len(s)//2+1):
            steps = k
            answer = ""
            value = 0
            tmp = ""
            for i in range(0, len(s), steps):
                if tmp == s[i:i+steps]:
                    value += 1
                else:
                    answer=check(value, tmp,answer)
                    value = 1
                    tmp = s[i:i+steps]
            answer=check(value, tmp,answer)
            if len(answer) < best:
                best = len(answer)
    return best

s = input().rstrip()
print(solution(s))