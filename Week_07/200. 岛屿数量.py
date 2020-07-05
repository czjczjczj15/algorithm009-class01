法一：深度优先搜索
法二：广度优先搜索(最快) (老师说：要手动维护一个queue队列)
法三：并查集（最慢的感觉）
########################################
# 第一次，failed
# （背）中国站：https://leetcode-cn.com/problems/number-of-islands/solution/pythonjavascript-tao-lu-dfs200-dao-yu-shu-liang-by/ #DFS法
        if not grid: return 0
        
        count = 0
        for i in range(len(grid)): # len(list)是先看行的数量
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count
    
    def dfs(self, grid, i, j): 
#         # 什么时候要用self?
#         # https://www.cnblogs.com/ydf0509/p/9435677.html
#         # 需要全局变量的时候用self
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return 
        grid[i][j] = '0'
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)
        
        # 时间复杂度O(m*n)
        # 空间复杂度O(m*n)
    
        # 国际站的：https://leetcode.com/problems/number-of-islands/discuss/56349/7-lines-Python-~14-lines-Java
        # def sink(i, j):
        #     if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
        #         grid[i][j] = '0'
        #         list(map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1)))
        #         return 1
        #     return 0
        # return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))
    
        # def sink(i, j):
        #     if 0 <= i < len(grid) and 0<= j < len(grid[0]) and grid[i][j] == '1': 
        #         grid[i][j] = '0'
        #         list(map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1)))
        # return sum(grid[i][j] == '1' and not sink(i,j) \
        #         for i in range(len(grid)) for j in range(len(grid[0])))
        
###################################
        # 第二次，failed
 # DFS
        if not grid: return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":      # 这里是“1”，不是1
                    self.dfs(i,j,grid)
                    count += 1
        return count

       
    def dfs(self, i,j, grid): # 这个def是写在和def numIslands一列上的
        if  i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] != "1": # 这里是“1”，不是1
            return 
        grid[i][j] = "0" # 这里是“0”，不是1
        
        self.dfs(i+1,j, grid)
        self.dfs(i-1,j, grid)
        self.dfs(i,j+1, grid)
        self.dfs(i,j-1, grid)

        # 时间复杂度：O(MN)
        # 空间复杂度： O(MN)（在最坏情况下，整个网格均为陆地，深度优先搜索的深度达到 M NMN）


# BFS, 考虑矩阵全 1 的情况，neighbors 维护的是矩阵的对角线，从左上往右下遍历，所以最大为 min(M,N)
# 注意，扩散是从左上角开始的，不是从中间，所以是min(M,N)
nr = len(grid)
if nr == 0:
    return 0
nc = len(grid[0])

num_islands = 0
for r in range(nr):
    for c in range(nc):
        if grid[r][c] == "1":
            num_islands += 1
            grid[r][c] = "0"
            # 用collections.deque()，不要用list
            # 用collections.deque()是68ms，用list是80ms
            # https://blog.csdn.net/qq_40991386/article/details/81150338,有提到deque的删除和增加的时间复杂度都是O(1), 而list是O(n)
            neighbors = collections.deque([(r, c)]) 
            while neighbors:
                row, col = neighbors.popleft()
                for x, y in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]: # 这样写简洁很多
                    if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                        neighbors.append((x, y))
                        grid[x][y] = "0"

return num_islands


# 并查集
class UnionFind:
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.count = 0
        self.parent = [-1] * (m * n)
        self.rank = [0] * (m * n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.parent[i * n + j] = i * n + j
                    self.count += 1
    
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] < self.rank[rooty]:
                rootx, rooty = rooty, rootx
            self.parent[rooty] = rootx
            if self.rank[rootx] == self.rank[rooty]:
                self.rank[rootx] += 1
            self.count -= 1
    
    def getCount(self):
        return self.count

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        uf = UnionFind(grid)
        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    grid[r][c] = "0"
                    for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                        if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                            uf.union(r * nc + c, x * nc + y)
        
        return uf.getCount()

# 1.时间复杂度：O(MN * \alpha(MN))O(MN∗α(MN))，其中 MM 和 NN 分别为行数和列数。注意当使用路径压缩（见 find 函数）和按秩合并（见数组 rank）实现并查集时，单次操作的时间复杂度为 \alpha(MN)α(MN)，其中 \alpha(x)α(x) 为反阿克曼函数，当自变量 xx 的值在人类可观测的范围内（宇宙中粒子的数量）时，函数 \alpha(x)α(x) 的值不会超过 55，因此也可以看成是常数时间复杂度。

# 2.空间复杂度：O(MN)O(MN)，这是并查集需要使用的空间。