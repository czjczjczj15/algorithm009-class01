class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:

        # https://leetcode-cn.com/problems/max-sum-of-rectangle-no-larger-than-k/solution/gu-ding-zuo-you-bian-jie-qian-zhui-he-er-fen-by-po/
        # 感觉是 前缀加二分 中比较好的答案了
        import bisect
        test = bisect.bisect_left([0,1,2,6,7,10], 5)
        print(test)
        row = len(matrix)
        col = len(matrix[0])
        res = float("-inf")
        for left in range(col):
            # 以left为左边界，每行的总和
            _sum = [0] * row
            
            for right in range(left, col):
                for j in range(row):
                    _sum[j] += matrix[j][right]
                # 在left，right为边界下的矩阵，求不超过K的最大数值和
                arr = [0]
                cur = 0
                for tmp in _sum:
                    cur += tmp
                    # 二分法
                    loc = bisect.bisect_left(arr, cur - k)
                    if loc < len(arr):res = max(cur - arr[loc], res)
                    # 把累加和加入
                    bisect.insort(arr, cur)
            print(_sum)
        return res

        # 国际站的留言的一个人的答案，速度很快，但是代码很长
        # https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/discuss/83596/Any-Accepted-Python-Solution

        # O(MlogM) method is called only when quick check is passed,
        # which should only be used when max sum > k and try to use ceiling to find a sum <= k
        def bstSearch(sum_list, k):
            currSum = 0
            bst = BST()
            bst.insert(0)
            for sum in sum_list:
                currSum += sum
                prevSum = bst.ceiling(currSum - k)
                self.maxSum = max(self.maxSum, currSum - prevSum)
                bst.insert(currSum)

        # O(M) method is called for quick check the max sum of any sub arrays
        def kadane(sum_list, k):
            maxSum = -(1<<31)
            currSum = 0
            for sum in sum_list:
                currSum = max(sum, sum + currSum)
                maxSum = max(maxSum, currSum)
            if maxSum <= k:
                self.maxSum = max(self.maxSum, maxSum)
                return False
            else:
                return True

        M = len(matrix)
        if M == 0: return 0
        N = len(matrix[0])
        if N == 0: return 0

        self.maxSum = -(1<<31)
        for left in range(N):
            sum_list = [0]*M
            for right in range(left, N):
                for i in range(M):
                    sum_list[i] += matrix[i][right]

                # O(M) method kadane is called for quick check
                # False means the max sum in any sub array <= k, so unnecessary to do bstSearch,
                # which should only be used when max sum > k and try to use ceiling to find a sum <= k
                if kadane(sum_list, k):
                    bstSearch(sum_list, k)

                # early temination condition
                if self.maxSum == k:
                    return k

        return self.maxSum
    
class BST:
    def __init__(self):
        self.root = {}
    
    def insert(self, value):
        if self.root:
            self._insert(self.root, value)
        else:
            self.root = {"value": value}
            
    def _insert(self, cur_node, value):
        if value < cur_node["value"]:
            if "left" in cur_node:
                self._insert(cur_node["left"], value)
            else:
                cur_node["left"] = {"value": value}
        else:
            if "right" in cur_node:
                self._insert(cur_node["right"], value)
            else:
                cur_node["right"] = {"value": value}
                
    def ceiling(self, value):
        cur_node = self.root
        result = 1 << 31
        while cur_node:
            if cur_node["value"] < value:
                cur_node = cur_node.get("right", None)
            else:
                result = min(result, cur_node["value"])
                cur_node = cur_node.get("left", None)
        return result