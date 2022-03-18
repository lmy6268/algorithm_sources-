#이분 탐색을 통한 시간 단축 
import sys;input=sys.stdin.readline
def binary_search(arr,target,st,en):
    if st>en:
        return None
    mid=(st+en)//2
    if arr[mid][:len(target)] == target:
        return mid
    if arr[mid][:len(target)] > target:
        return binary_search(arr, target, st, mid-1)
    elif arr[mid][:len(target)] < target:
        return binary_search(arr, target, mid+1, en)


n,m=map(int,input().split())
res=0 #최종 출력할 값
s=[input().rstrip() for _ in range(n)]
s.sort()
for _ in range(m):
    prefix=input().rstrip()
    if binary_search(s, prefix, 0, n-1)!=None:
        res+=1
print(res)






# #트라이 연습 
# import sys;input=sys.stdin.readline
# #노드 클래스
# class Node:
#     def __init__(self, key, data=None):
#         self.key = key
#         self.data = data
#         self.children = {}

# #트라이 클래스
# class Trie:
#     def __init__(self):
#         self.head = Node(None)

#     def insert(self,string):
#         curr_node = self.head

#         for char in string:
#             #자식Node 들 중 같은 문자가 없다면 Node 새로 생성
#             if char not in curr_node.children:
#                 curr_node.children[char]=Node(char)
#                 print(char,curr_node.children)


#             #같은 문자가 있다면 노드를 따로 생성하지 않고 해당 노드로 이동
#             curr_node = curr_node.children[char]
#         #문자열이 끝난 지점의 노드의 data값에 해당 문자열을 표시
#         curr_node.data=string
        
#     #문자열이 존재하는지 탐색한다.
#     def search(self,string):
#         #가장 아래의 있는 노드부터 탐색을 시작
#         curr_node= self.head
#         for char in string:
#             if char in curr_node.children:
#                 curr_node=curr_node.children[char]
#             else:
#                 return False
#         # 탐색이 끝난 후에 해당 노드의 data값이 존재한다면
#         # 문자가 포함되어있다는 뜻이다!
#         if curr_node.data is not None:
#             return True

# n,m=map(int,input().split())
# res=0 #최종 출력할 값

# trie=Trie()
# for _ in range(n):
#     s=input().rstrip()
#     trie.insert(s)
# for _ in range(m):
#     ts=input().rstrip()
#     if trie.search(ts):
#         res+=1
