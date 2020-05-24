学习笔记

数组笔记：
数组里面是可以装不同的类型的数据，这叫叫泛型。
数组在计算机里用连续的地址储存。
数组可以随机访问任何一个元素，所以访问时间非常快，时间复杂度是O(1)
问题在于增加和删除数组的时候，时间复杂度是O(n)（最差是移动整个数组n，最好的情况是插在最后那里O(1)）。

时间复杂度：
prepend O(1)
append  O(1)
lookup  O(1)
insert  O(n)
delete  O(n)

数组的增加和删除的时间复杂度都是O(n)，为了减少时间复杂度，有些题可以尽量用交换元素的方法去实现，比如move zeros那道题。
查询一个元素是否再数组里面，可以用二分法，时间复杂度是O(logn)，前提是数组是有序的。


链表笔记：
类型有：
1.	单链表：只有一个next指针
2.	双向链表
3.	循环链表：tail指向head


链表的时间复杂度：
prepend	O(1)
append	O(1)
lookup	O(n)
insert	O(1): 链表增加一个元素，先把上一个的next指向新加的node的value，然后新加的node指向下一个node的值。
delete	O(1)


跳表笔记：
查询一个元素是否在列表里的时间复杂度是O(n)，为了更快的找到元素，我们可以用跳表。
跳表的特点是：
1.有序的链表。
2.对标的是平衡树（AVL Tree）和二分查找， 是一种 插入/删除/搜索 都是 O(log n) 的数据结构。
3.最大的优势是原理简单、容易实现、方便扩展、效率更高。因此 在一些热门的项目里用来替代平衡树，如 Redis、LevelDB 等。
4.有很多级的索引，使得跳表的搜索时间复杂度是O(logn)
5.跳表有升维思想和用空间换时间思想。

跳表的时间复杂度：
lookup: O(logn)
insert: O(logn)
delete: O(logn)

为什么Redis选择使用跳表而不是红黑树来实现有序集合？
Redis 中的有序集合(zset) 支持的操作：
1.插入一个元素
2.删除一个元素
3.查找一个元素
4.有序输出所有元素
5.按照范围区间查找元素（比如查找值在 [100, 356] 之间的数据）
其中，前四个操作红黑树也可以完成，且时间复杂度跟跳表是一样的。但是，按照区间来查找数据这个操作，红黑树的效率没有跳表高。按照区间查找数据时，跳表可以做到 O(logn) 的时间复杂度定位区间的起点，然后在原始链表中顺序往后遍历就可以了，非常高效。

来源：https://juejin.im/post/5d90e4a15188252d3a6a60b8


其他笔记：
1.logn 以什么为底？
在很多时候是2 比如2分的情况，红黑树检索的情况 但比如3分法就是以3为底了，在n很大的时候以不同数为底，相差的其实就是一个常数的倍数 所以都用logn描述这类复杂度


#################################
阅读python源代码
################################
1. stack 
在python中是用list来实现stack的，stack的特点是先进后出
当进栈的时候，用append()
当出栈的时候，用pop()

实现的代码可以是类似这样的：
class Stack:

    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def size(self):
        return len(self.stack)

链接：https://stackabuse.com/stacks-and-queues-in-python/



2. queue
queue也是可以用list来实现的，特点是先进先出

class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue) 
链接：https://stackabuse.com/stacks-and-queues-in-python/

python 中有queue这个库可以用的
创建一个queue的方法是：
import threading, queue
q = queue.Queue()

其中有几种不同类型的class:
1. queue.Queue
2. queue.LifoQueue
3. queue.PriorityQueue
4. queue.SimpleQueue


其中， Queue, LifoQueue, or PriorityQueue 提供一下的方法：

Queue.qsize()
Queue.empty()
Queue.full()
Queue.put(item, block=True, timeout=None)
Queue.put_nowait(item)
Queue.get(block=True, timeout=None)
Queue.get_nowait()
Queue.task_done()
Queue.join()


如果我们要创建双端队列，可以
from collections import deque

deque提供一下方法：
append(x)                 把元素加到队列的右边
appendleft(x)             把元素加到队列的左边
clear()                   清理所有的元素 
copy()                    复制整个双端队列
count(x)                   数等于x的元素的个数
extend(iterable)           把元素一个个地加入队列的右边
extendleft(iterable)       把元素一个个反顺序地加入队列的左边
index(x[, start[, stop]])
insert(i, x)
pop()
popleft()
remove(value)
reverse()
rotate(n=1)
maxlen





