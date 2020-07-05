# DFS 时间复杂度：O(n^2)，整个矩阵都要被遍历，大小为 n^2。空间复杂度：O(n)O(n)，visitedvisited 数组的大小。
# BFS 时间复杂度：O(n^2)，整个矩阵都要被访问。空间复杂度：O(n)O(n)，queuequeue 和 visitedvisited 数组的大小。
# 并查集
####################################################

# 第一次，failed
#并查集，极客大学老师代码
# 时间复杂度：O(n^3)，访问整个矩阵一次，并查集操作需要最坏 O(n)O(n) 的时间。
# 空间复杂度：O(n)，parentparent 大小为 nn。

if not M: return 0

n = len(M)
p = [i for i in range(n)] # 并查集创建起来
# print(p)

for i in range(n): # 遍历矩阵
    for j in range(n):
        if M[i][j] == 1:
            self._union(p, i ,j) # 合并i,j
            print(p)

return len(set([self._parent(p,i) for i in range(n)])) # 看整个n里面有多少的parent

def _union(self, p ,i ,j ):
p1 = self._parent(p,i)
p2 = self._parent(p, j)
p[p2] = p1

def _parent(self, p, i):
root = i
while p[root] != root:
    root = p[root]
while p[i] != i:
    x = i; i = p[i]; p[x] = root
return root