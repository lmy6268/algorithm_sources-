import sys; p=sys.stdin.readline
n=int(p())
player=list(map(int,p().split()))
J=player.pop(0)
player.sort()
for i in player:
    if J>i:
        J+=i
    else:
        print("No")
        sys.exit()
print("Yes")