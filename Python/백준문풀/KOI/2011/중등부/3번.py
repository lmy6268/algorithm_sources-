import sys;input=sys.stdin.readline
n=int(input())
st=[[]]
d=[[0]*(n+1) for _ in range(n+1)]
res=0
for i in range(n):
    st.append(list(map(int,input().split()[:-1])))

def dp(start,end):
    if start==end:
        return 0
    elif start<end:
        
        res=dp(start,)
        