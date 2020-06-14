学习笔记

## 深度优先和广度优先

搜索一般都是暴力的搜索
如果数据集本身是没有什么特点，那么我们会遍历每个值。
在树状图中寻找特定值的方法：
1.每个节点访问一次
2.每个节点仅仅访问一次
3.对于节点的访问顺序不同课分为：
  a.深度优先：depth first search
  b.广度优先：breath first search

优先级优先搜索，一般称为启发式搜索（更多是深度学习方面的）
优先级优先现在已经用于推荐算法和高级的搜索算法
示例代码：
def dfs(node):
    #一开始是递归的终止条件：
    if node in visited:
        # already visited
        return 

    visited.add(node)
    # process current node，访问当前层
    # ... # logic here
    
    # 往下访问：
    # 如果是二叉树的话，就是左孩子和右孩子；如果是图的话，就是它的联通的相邻节点；如果是多叉树的话就是遍历children，把所有的children遍历一次。
    dfs(node.left)
    dfs(node.right)

DFS递归写法：

visited = set()
def dfs(node, visited):
    visited.add(node)
    # process current node here.
    ...
    for next_node in node.children():
    	# 如果是多叉树的话也适用
        if not next_node in visited:
            dfs(next_node, visited)

一开始传root进来，root就会先放到visited里面，表示root已经被visit
被visited后，就在root.children里面找最左边未被访问的next_node

BFS代码结构：
def BFS(graph. start, end):
	queue = []
	queue.append([start])
	visited.add(start)

	while queue:
		node = queue.pop()
		visited.add(node)

		process(node)
		nodes = generate_related_nodes(node)
		queue.push.(nodes)

	# other processing work
	...

在java里面用链表，或者是用一个双端队列deque来表示。
在python里可以用列表，或者用deque。
DFS和BFS的本质就是把所有的node都遍历一遍，只不过顺序不同而已。

## 贪心算法
贪心算法是一种在每一步选择中都采取在当前状态下最好或最优（即最有 利）的选择，从而希望导致结果是全局最好或最优的算法。 
贪心算法与动态规划的不同在于它对每个子问题的解决方案都做出选择，不能回退。动态规划则会保存以前的运算结果，并根据以前的结果对当前进行 选择，有回退功能。
贪心法可以解决一些最优化问题，如：求图中的最小生成树、求哈夫曼编码等。然而对于工程和生活中的问题，贪心法一般不能得到我们所要求的答案。 
一旦一个问题可以通过贪心法来解决，那么贪心法一般是解决这个问题的最好办法。由于贪心法的高效性以及其所求得的答案比较接近最优结果，贪心 法也可以用作辅助算法或者直接解决一些要求结果不特别精确的问题。
 
 
适用贪心算法的场景：
简单地说，问题能够分解成子问题来解决，子问题的最优解能递推到最终 问题的最优解。这种子问题最优解称为最优子结构。
贪心算法与动态规划的不同在于它对每个子问题的解决方案都做出选择，不能回退。动态规划则会保存以前的运算结果，并根据以前的结果对当前 进行选择，有回退功能。


## 二分查找的前提：
1. 目标函数单调性（单调递增或者递减）

2. 存在上下界（bounded）

3. 能够通过索引访问（index accessible)

代码模板：
########
left, right = 0, len(array) - 1

while left <= right:
	mid  = (left + right ) / 2
	if array[mid] == target:
		# find the target!!
		break or return reuslt
 	elif array[mid] < target:
 		left = mid + 1
 	else: 
 		right = mid - 1



