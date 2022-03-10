N, num = map(int,input().split())

def solution(N, num):
    dp = [0, [N]]+[[int(str(N)*i)] for i in range(2, 9)]
    t = ['*', '//', '+', '-']
    if num==N:
        return 1
    for i in range(2, 9):
        for j in range(1, i):
            for x in dp[j]:
                for y in dp[i-j]:
                    for v in t:
                        try: #피연산자가 0인경우 오류 발생 
                            if 0 < (a := eval((str(x)+v+str(y)))) <= 32000:
                                    dp[i].append(a)
                        except:
                            pass
        dp[i] = list(set(dp[i]))
        if int(num) in dp[i]:
            return i
    return -1

print(solution(N, num))