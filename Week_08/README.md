学习笔记

位运算：

1. 将x 最右边的n 位清零：x& (~0 << n)
2. 获取x 的第n 位值（0 或者1）：(x >> n) & 1
3. 获取x 的第n 位的幂值：x& (1 <<n)
4. 仅将第n 位置为1：x | (1 << n)
5. 仅将第n 位置为0：x & (~ (1 << n))
6. 将x 最高位至第n 位（含）清零：x& ((1 << n) -1)
7. 将第n 位至第0 位（含）清零：x& (~ ((1 << (n + 1)) -1))

实战位运算要点

• 判断奇偶： x % 2 == 1  —> (x & 1) == 1 x % 2 == 0  —> (x & 1) == 0 
• x >> 1 —> x / 2.     即： x = x / 2;   —>    x = x >> 1; mid = (left + right) / 2;   —>    mid = (left + right) >> 1; 
• X = X & (X-1) 清零最低位的1 
• X & -X => 得到最低位的1 
• X & ~X => 0

N皇后的位运算解法-Python

	def totalNQueens(self, n): 
		if n < 1: return [] 
		self.count = 0 
		self.DFS(n, 0, 0, 0, 0) 
		return self.count
	def DFS(self, n, row, cols, pie, na): 
		# recursion terminator 
		if row >= n: 
			self.count += 1 
			return
		bits = (~(cols | pie | na)) & ((1 << n) — 1)  # 得到当前所有的空位

		while bits: 
			p = bits & —bits # 取到最低位的1 
			bits = bits & (bits — 1) # 表示在p位置上放入皇后 
			self.DFS(n, row + 1, cols | p, (pie | p) << 1, (na | p) >> 1) 
			# 不需要revert cols, pie, na 的状态


布隆过滤器:

Bloom Filter vs Hash Table:

一个很长的二进制向量和一系列随机映射函数。布隆过滤器可以用于检索 一个元素是否在一个集合中。 
优点是空间效率和查询时间都远远超过一般的算法， 
 
缺点是有一定的误识别率和删除困难。

Python 实现:

	from bitarray import bitarray 
	import mmh3 
	class BloomFilter: 
		def __init__(self, size, hash_num): 
			self.size = size 
			self.hash_num = hash_num 
			self.bit_array = bitarray(size) 
			self.bit_array.setall(0) 

		def add(self, s): 
			for seed in range(self.hash_num): 
				result = mmh3.hash(s, seed) % self.size 
				self.bit_array[result] = 1 

		def lookup(self, s): 
			for seed in range(self.hash_num): 
				result = mmh3.hash(s, seed) % self.size 
				if self.bit_array[result] == 0: 
					return "Nope" 
			return "Probably" 

	bf = BloomFilter(500000, 7) 
	bf.add("dantezhao") 
	print (bf.lookup("dantezhao")) 
	print (bf.lookup("yyj")) Python 

LRU Cache：

• 两个要素： 大小 、替换策略

• Hash Table + Double LinkedList

• O(1) 查询 O(1) 修改、更新

	class LRUCache(object): 
		def __init__(self, capacity): 
			self.dic = collections.OrderedDict() 
			self.remain = capacity 

		def get(self, key): 
			if key not in self.dic: 
				return -1 
			v = self.dic.pop(key) 
			self.dic[key] = v   # key as the newest one 
			return v 

		def put(self, key, value): 
			if key in self.dic: 
				self.dic.pop(key) 
			else: 
				if self.remain > 0: 
					self.remain -= 1 
				else:   # self.dic is full 
					self.dic.popitem(last=False)
			self.dic[key] = value



排序算法：

1.	比较类排序： 
 
通过比较来决定元素间的相对次序，由于其时间复杂度不能突破 O(nlogn)，因此也称为非线性时间比较类排序。 

2.	非比较类排序： 
 
不通过比较来决定元素间的相对次序，它可以突破基于比较排序的时 间下界，以线性时间运行，因此也称为线性时间非比较类排序。

初级排序 - O(n^2)：

1. 选择排序（Selection Sort） 每次找最小值，然后放到待排序数组的起始位置。

2.插入排序（Insertion Sort） 从前到后逐步构建有序序列；对于未排序数据，在已排序序列中从后 向前扫描，找到相应位置并插入。

3.冒泡排序（Bubble Sort） 嵌套循环，每次查看相邻的元素如果逆序，则交换。


高级排序 - O(N*LogN)：

• 快速排序（Quick Sort） 
 
数组取标杆 pivot，将小元素放 pivot左边，大元素放右侧，然后依次 对右边和右边的子数组继续快排；以达到整个序列有序。

高级排序 - O(N*LogN)

• 归并排序（Merge Sort）— 分治 
 
	1. 把长度为n的输入序列分成两个长度为n/2的子序列； 	2. 对这两个子序列分别采用归并排序； 	3. 将两个排序好的子序列合并成一个最终的排序序列。 

高级排序 - O(N*LogN)

归并 和 快排 具有相似性，但步骤顺序相反

归并：先排序左右子数组，然后合并两个有序子数组 
 
快排：先调配出左右子数组，然后对于左右子数组进行排序

高级排序 - O(N*LogN)

• 堆排序（Heap Sort） — 堆插入 O(logN)，取最大/小值 O(1) 
 
	1. 数组元素依次建立小顶堆  
	2. 依次取堆顶元素，并删除 

特殊排序 - O(n)

• 计数排序（Counting Sort） 计数排序要求输入的数据必须是有确定范围的整数。将输入的数据值转化为键存 储在额外开辟的数组空间中；然后依次把计数大于 1 的填充回原数组

• 桶排序（Bucket Sort） 桶排序 (Bucket sort)的工作的原理：假设输入数据服从均匀分布，将数据分到有 限数量的桶里，每个桶再分别排序（有可能再使用别的排序算法或是以递归方式 继续使用桶排序进行排）。

• 基数排序（Radix Sort） 基数排序是按照低位先排序，然后收集；再按照高位排序，然后再收集；依次类 推，直到最高位。有时候有些属性是有优先级顺序的，先按低优先级排序，再按 高优先级排序。
 





