学习笔记

字典树:

1. 字典树的数据结构

2. 字典树的核心思想

3. 字典树的基本性质

二叉树：有两个子节点的树
多叉树：有多个子节点的树
二叉搜索树：
1.是子树的关系，不是儿子和父亲的关系。
任何一个节点，它的左子树的所有节点都要小于这个根节点，右子树的所有节点都要大于根节点。且对于任何子树都满足这个特性。
2.对其进行中序遍历的话，会得到递增的数组。所以查找的效率更高。

并查集：

判断两个个体是不是在一个集合当中。
适用场景：判断两个人是不是好友。组团、配对等。

基本操作：

• makeSet(s)：建立一个新的并查集，其中包含 s 个单元素集合。

• unionSet(x, y)：把元素 x 和元素 y 所在的集合合并，要求 x 和 y 所在 的集合不相交，如果相交则不合并。

• ﬁnd(x)：找到元素 x 所在的集合的代表，该操作也可以用于判断两个元 素是否位于同一个集合，只要将它们各自的代表比较一下就可以了。

并查集实现原理：
1.初始话：一开始每一个元素拥有一个parent数组指向自己，表示自己是自己的集合。
2.查询，合并。
查询方法是看每个元素的parent，然后再接着看parent，知道parent等于它自己的时候，说明找到他的集合的领头元素，就找到集合是属于谁。
合并的方法是把一个领头元素指向另一个领头元素，
3。路径压缩：把一条路径上的所有元素指向他们的领头元素，这样查询时间可以快很多，只要一步即可。

并查集模板：
    def init(p):
        # for i = 0 .. n: p[i] = i
        p = [i for i in range(n)]

    def union(self, p, i, j):
        p1 = self.parent(p,i)
        p2 = self.parent(p,j)
        p[p1] = p2

    def parent(self, p, i):
        root = i
        while p[root] != root:
            root = p[root]
        while p[i] != i: # 路径压缩？
            x = i; i= p[i]; p[x] = root
        return root

初级搜索：
1.朴素搜索
2.优化方式：不重复(fibonacci)，减枝（生成括号问题）。办法是：用数组存中间值；用顺推的办法，避免重复中间的重复的状态，把重复性给去掉。
3.搜索方向：DFS（用栈，类似于傻搜索，知道撞到南墙才回头）, BFS（用队列，起码有最近距离）。

高级搜索：
1.双向搜索：起点和终点分别做一个广度优先，然后在中间相遇，这样时间更快。
2.启发式搜索（优先级搜索）：不是用栈，不是用队列，而是用优先队列。
按照节点的优先级排列的，把那些更有可能对我们有帮助的节点先拿出来，这个叫A*算法。

回溯法：
回溯法采用试错的思想，它尝试分步的去解决一个问题。在分步解决问题的过程中，当 它通过尝试发现现有的分步答案不能得到有效的正确的解答的时候，它将取消上一步甚 至是上几步的计算，再通过其它的可能的分步解答再次尝试寻找问题的答案。

回溯法通常用最简单的递归方法来实现，在反复重复上述的步骤后可能出现两种情况：

• 找到一个可能存在的正确的答案

• 在尝试了所有可能的分步方法后宣告该问题没有答案

在最坏的情况下，回溯法会导致一次复杂度为指数时间的计算。

剪枝：
8皇后问题：只要colomn被占了，或者撇被占了，或者捺被占了，就马上进行剪枝。
八皇后代码：

    def solveNQueens(self, n): 
        if n < 1: return [] 
        self.result = [] 
        self.cols = set(); self.pie = set(); self.na = set() 
        self.DFS(n, 0, []) 
        return self._generate_result(n) 

    def DFS(self, n, row, cur_state): 
        # recursion terminator 
        if row >= n: 
            self.result.append(cur_state) 
            return 

        for col in range(n): 
            if col in self.cols or row + col in self.pie or row - col in self.na: # go die! 
                continue 
                # update the flags 
            self.cols.add(col) 
            self.pie.add(row + col) 
            self.na.add(row - col) 

            self.DFS(n, row + 1, cur_state + [col]) 

            self.cols.remove(col) 
            self.pie.remove(row + col) 
            self.na.remove(row - col) 

启发式搜索：基于BFS，用优先队列去搜索。
A* search 启发式搜索模板：

    def AstarSearch(graph, start, end): 
        pq = collections.priority_queue() # 优先级 —> 估价函数  
        pq.append([start])   
        visited.add(start)  

        while pq:    
            node = pq.pop() # can we add more intelligence here ?   
            visited.add(node)   
            process(node)    
            nodes = generate_related_nodes(node)     
            unvisited = [node for node in nodes if node not in visited]   
            pq.push(unvisited) 


估价函数：
启发式函数： h(n)，它用来评价哪些结点最有希望的是一个我们要找的结点，h(n)会返回一个非负实数,也可以认为是从结点n的目标结点路径的估计成本。

启发式函数是一种告知搜索方向的方法。它提供了一种明智的方法来猜测哪个邻居结点会导向一个目标。


平衡树：
二叉搜索树有n层的话，那么搜索的时间复杂度是O(n)
如果是总的节点数是n的话，那么搜索的时间复杂度是O(log2n)
会出现一种极端的情况，就是在插入的时候，值一直插入左孩子，这样二叉搜索树就退化成一个链表了。
所以为了避免这种情况的出现，就有了平衡二叉树的出现。
https://en.wikipedia.org/wiki/Self-balancing_binary_search_tree
平衡树有很多种类，有
2–3 tree,AA tree,AVL tree,B-tree,Red–black tree,Scapegoat tree,Splay tree,Treap,Weight-balanced tree
在每一步插入删除的时候，都去判断是否平衡。

AVL树：
1. 发明者G. M. Adelson-Velsky和Evgenii Landis
2. Balance Factor（平衡因子）： 是它的左子树的高度减去它的右子树的高度（有时相反）。 balance factor = {-1, 0, 1}
   注意是高度，不是左子树的结点数或者是右子树的结点数，只是他的高度。因为二叉搜索树查询效率只于高度有关，和结点的个数是没有关系的。
3. 通过旋转操作来进行平衡（四种）
4. https://en.wikipedia.org/wiki/Self-balancing_binary_search_tree
5. 不足：结点需要存储额外信息，且调整次数频繁。

AVL树的由来：因为查询的时间是等于树的深度的，所以我们记录深度差，能得到平衡因子，平衡因子不平衡的时候，我们要做四种平衡操作。


红黑树：近似平衡二叉树

红黑树是一种近似平衡的二叉搜索树（BinarySearch Tree），它能够确保任何一 个结点的左右子树的高度差小于两倍。具体来说，红黑树是满足如下条件的二叉 搜索树：
• 每个结点要么是红色，要么是黑色
• 根结点是黑色
• 每个叶结点（NIL结点，空结点）是黑色的。
• 不能有相邻接的两个红色结点
• 从任一结点到其每个叶子的所有路径都包含相同数目的黑色结点。

关键性质：
从根到叶子的最长的可能路径不多于最短的可能路径的两倍长。

对比：
• AVL trees providefaster lookupsthan Red Black Trees because they are more strictly balanced. (AVL树能更快地查找)
• Red Black Trees providefaster insertion and removaloperations than AVL trees as fewer rotations are done due to relatively relaxed balancing. （红黑树删除和增加要更快）
• AVL trees storebalance factors or heightswith each node, thus requires storage for an integer per node whereas Red Black Tree requires only 1 bit of information per node. （AVL要用更多的内存来存factor和height）
• Red Black Trees are used in most of the language libraries likemap,multimap,multisetin C++whereas AVL trees are used indatabaseswhere faster retrievals are required. (在读操作更多的情况下，用AVL。存和删更多的情况下，用红黑树)

C++,JAVA的map，set都是用红黑树。DB（比如刷微博），读的多，写的少，这样database一般用AVL








