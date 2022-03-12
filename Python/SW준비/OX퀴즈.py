import sys;input=sys.stdin.readline
for _ in range(int(input())):
    line=list(input().rstrip())
    score=0
    bonus=0
    combo=False
    for i in line:
        if i=='X':
            combo=False
            bonus=0
        else:
            if combo:
                bonus+=1
            else:
                combo=True
                bonus+=1
            score+=bonus
    print(score)
    