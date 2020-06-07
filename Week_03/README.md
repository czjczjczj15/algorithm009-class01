学习笔记

1.递归的实现，特性以及思维要点。

树很多都是递归来求解的。节点的定义本身就是用递归来定义的。

二叉搜索树：左子树都要小于根节点，右子树都要小于根节点。且左右子树都满足以上的特点。

计算机语言在创造的时候就是汇编，然后汇编有个特点就是没有循环嵌套，而是用递归。

递归的四个要点：
1.写递归先写终止条件
2.然后写处理层
3.然后到下一层
4.（清理当前层）

def recursion(level,param1,param2,...):
	# recusion terminator
	if level > MAX_LEVEL:
		process_result
		return

	# process logic in current level
	process(level,data...)

	# drill down
	self.recursion(level+1,p1,...)

	# reverse the current level status if needed

多递归时递归：
1.	尽量不要人肉递归
2.	找到最近重复子问题，
3.	数学归纳法的思维，当n成立的时候，n+1也成立
4.	递归的过程中可以加一些有用的if 条件，可以达到剪枝的效果。


2.分治，回溯的实现和特性：
分治和回溯的本质就是一种特殊的递归。遇到分治和回溯的题目要想到找重复性。重复性有最近的重复性和最优的重复性这些说法，最优的重复性就是动态规划。

做分治的题就是要找到大问题的子问题，找重复性，分解问题，最后组合每个子问题的结果。

分治的代码模板：
def divie_comquer(problem, param1, param2,...):
	# recursioin terminator
	if problem is None:
		print_resut
		return

	# prepare data
	data = prepare_data(problem)
	subproblems = split_problem(problem, data)

	# conquer subproblems
	subresult1 = self.divide_conquer(subproblems[0], p1,...)
	subresult2 = self.divide_conquer(subproblems[1], p1,...)
	subresult3 = self.divide_conquer(subproblems[2], p1,...)
    ...
    # process and generate the final result 
    result  = process_result(subresult1, subresult2, subresult3,...)











