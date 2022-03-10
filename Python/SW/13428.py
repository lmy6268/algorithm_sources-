# import sys;input=sys.stdin.readline
# for _ in range(int(input().rstrip())):
#     text=input().rstrip()
#     arr={int(text)}
#     for i in range(len(text)):
#         tmp=list(text)
#         for j in range(len(text)):
#             if i!=j:
#                 tmp[i],tmp[j]=tmp[j],tmp[i]#swap
#                 if tmp[0]!='0':
#                     arr.add(int("".join(tmp)))
#     print(min(arr),max(arr))
for T in range(int(input().strip())):
    text=input().rstrip()
    arr={int(text)}
    t=list(text)
    for i in range(len(text)):
        for j in range(len(text)):
            tmp=t[:]
            if i!=j:
                tmp[i],tmp[j]=tmp[j],tmp[i]#swap
                if tmp[0]!='0':
                    arr.add(int("".join(tmp)))
    print(f"#{T+1}",min(arr),max(arr))