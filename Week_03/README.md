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











