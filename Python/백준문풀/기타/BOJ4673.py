d=[[] for i in range(10001)]
for i in range(1,10001):
    s=i
    i=str(i)
    s+=sum([int(k) for k in i]) #각 자리수 더해주고
    if s<=10000:
        d[s].append(i)
for i in range(1,10001):
    if d[i]==[]:
        print(i)

