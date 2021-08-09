# 정렬
import sys
p = sys.stdin.readline


def sort(array):
    a = sorted(array.items())
    for i in a:
        if isinstance(i[1], list):
            idx = 0
            tmp = []
            for j in range(len(i[1])):
                if i[1][j] in extension:
                    i[1][idx], i[1][j] = i[1][j], i[1][idx]
                    idx += 1
                    tmp.append(i[1][j])
        
            if idx>=2:
                
                tmp.sort()
                for k in range(idx):
                    i[1][k]=tmp[k]
    a=dict(a)
    for key, value in a.items():
        if isinstance(value, list):
            for i in value:
                print(f"{key}.{i}")
        else:
            print(f"{key}.{value}")        


n, m = map(int, p().rstrip().split())  # n: 파일 개수 / m:확장자 개수
files = dict()
extension = []
for i in range(n):
    a, b = p().rstrip().split(".")
    if a in files:
        tmp = files.get(a)
        files[a] = [b, tmp]
    else:
        files[a] = b
for i in range(m):
    extension.append(p().rstrip())
extension.sort()
sort(files)
