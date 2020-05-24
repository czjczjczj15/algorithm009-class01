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

Queue的源码可以在以下网址找到：
https://github.com/python/cpython/blob/2.7/Lib/Queue.py

Queue源码分析：

class Queue:

    """Create a queue object with a given maximum size.
    If maxsize is <= 0, the queue size is infinite.
    """
    def __init__(self, maxsize=0):
        self.maxsize = maxsize # 队列的最大容量
        # 初始化队列对象的底层数据结构，该数据结构用来保存put到队列中的元素, 在Queue中，底层数据结构是collections.dequeue（双端队列）
        self._init(maxsize) 
        

        #在使用队列对象暴漏出的所有的方法时，都应该先获取到这个互斥变量,所有的获取了该互斥变量的方法，
        # 在它返回之前，都应该先释放该变量,这个互斥变量会在三个条件变量之间共享
        #（也就是说，这三个条件变量,的底层锁都是该互斥变量）。
        # 因此，获取这些条件变量时，会先获取到该互斥变量,释放这些条件变量时，会先释放该互斥变量。
        self.mutex = _threading.Lock()

        当成功地向队列中put一个元素时，会通知该条件变量；
        # 当以阻塞的方式从队列中get元素的时候，
        # 如果队列中没有可用的元素，那么线程会进入到该条件变量的waiting池，等待到超时或被唤醒
        self.not_empty = _threading.Condition(self.mutex)
       
        当成功地从队列中get一个元素时，会通知该条件变量。
        # 当以阻塞的方式向队列中put元素的时候，
        # 如果队列中没有剩余的空间，那么线程会进入到该条件变量的waiting池，等待到超时或被唤醒
        self.not_full = _threading.Condition(self.mutex)

        # 当未完成任务数归零的时候，会通知该条件变量，
        # join()操作会从阻塞状态中退出
        self.all_tasks_done = _threading.Condition(self.mutex)

        # 未完成的任务数
        self.unfinished_tasks = 0

    def task_done(self):
        """Indicate that a formerly enqueued task is complete.
        Used by Queue consumer threads.  For each get() used to fetch a task,
        a subsequent call to task_done() tells the queue that the processing
        on the task is complete.
        If a join() is currently blocking, it will resume when all items
        have been processed (meaning that a task_done() call was received
        for every item that had been put() into the queue).
        Raises a ValueError if called more times than there were items
        placed in the queue.
        """
        """调用该方法意味着，之前放到队列中的一个任务被完成了。
        该方法是被队列的消费者线程使用的。消费者线程在调用get()方法，从队列中获取到一个任务，
        并处理之后，需要调用该方法，告诉队列该任务处理完成了。
        每次，成功向队列中put一个元素的时候，都会将unfinished_tasks增加1；
        每次，调用task_done()方法，都会将unfinished_tasks减少1
        该方法的作用是唤醒正在阻塞的join()操作。
        """
        # 获取条件变量
        self.all_tasks_done.acquire()
        try:
            unfinished = self.unfinished_tasks - 1
            if unfinished <= 0:
                # 当unfinished小于0时，
                # 也就是成功调用put()的次数小于调用task_done()的次数时，会抛出异常
                if unfinished < 0:
                    raise ValueError('task_done() called too many times')
                # 当unfinished为0时，会通知all_tasks_done
                self.all_tasks_done.notify_all()
            # 递减unfinished_tasks
            self.unfinished_tasks = unfinished
        finally:
            # 释放条件变量
            self.all_tasks_done.release()

    def join(self):
        """Blocks until all items in the Queue have been gotten and processed.
        The count of unfinished tasks goes up whenever an item is added to the
        queue. The count goes down whenever a consumer thread calls task_done()
        to indicate the item was retrieved and all work on it is complete.
        When the count of unfinished tasks drops to zero, join() unblocks.
        """
        """该方法会一直阻塞，直到，队列中所有的元素都被取出，并被处理了。
        当成功向队列中put元素的时候，unfinished_tasks会增加。
        当消费者线程调用task_done()方法时，unfinished_tasks会减少。
        当unfinished_tasks降为0时，join()方法才会退出阻塞状态
        """
        self.all_tasks_done.acquire()
        try:
            while self.unfinished_tasks:
                self.all_tasks_done.wait()
        finally:
            self.all_tasks_done.release()
    
    def qsize(self):
        """Return the approximate size of the queue (not reliable!)."""
        self.mutex.acquire()
        n = self._qsize()
        self.mutex.release()
        return n

    #如果队列为空，则返回True，否则返回False
    def empty(self):
        """Return True if the queue is empty, False otherwise (not reliable!)."""
        self.mutex.acquire()
        n = not self._qsize()
        self.mutex.release()
        return n

    #如果队列满了，则返回True，否则返回False
    def full(self):
        """Return True if the queue is full, False otherwise (not reliable!)."""
        self.mutex.acquire()
        n = 0 < self.maxsize == self._qsize()
        self.mutex.release()
        return n

    def put(self, item, block=True, timeout=None):
        #在这里，往队列中加入一个元素，如果block参数是True，并且timeout参数是None，
        那么put操作会阻塞，直到队列中有空闲的空间。
        如果block参数是True，timeout参数是非负数，
        并且，在这个期间，队列中一直没有空间，那么put操作会阻塞
        到超时，然后抛出Full异常。
        如果block参数是False，并且队列中有空闲空间，
        那么会立即把元素保存到底层数据结构中；否则，会忽略掉timeout参数，
        抛出Full异常。
        """Put an item into the queue.
        If optional args 'block' is true and 'timeout' is None (the default),
        block if necessary until a free slot is available. If 'timeout' is
        a non-negative number, it blocks at most 'timeout' seconds and raises
        the Full exception if no free slot was available within that time.
        Otherwise ('block' is false), put an item on the queue if a free slot
        is immediately available, else raise the Full exception ('timeout'
        is ignored in that case).
        """
        self.not_full.acquire()
        try:
            if self.maxsize > 0:
                if not block:
                    if self._qsize() == self.maxsize:
                        raise Full
                elif timeout is None:
                    while self._qsize() == self.maxsize:
                        self.not_full.wait()
                elif timeout < 0:
                    raise ValueError("'timeout' must be a non-negative number")
                else:
                    endtime = _time() + timeout
                    while self._qsize() == self.maxsize:
                        remaining = endtime - _time()
                        if remaining <= 0.0:
                            raise Full
                        self.not_full.wait(remaining)
            self._put(item)
            self.unfinished_tasks += 1
            self.not_empty.notify()
        finally:
            self.not_full.release()

    # 非阻塞的put
    def put_nowait(self, item):
        """Put an item into the queue without blocking.
        Only enqueue the item if a free slot is immediately available.
        Otherwise raise the Full exception.
        """
        return self.put(item, False)

    def get(self, block=True, timeout=None):
        """Remove and return an item from the queue.
        If optional args 'block' is true and 'timeout' is None (the default),
        block if necessary until an item is available. If 'timeout' is
        a non-negative number, it blocks at most 'timeout' seconds and raises
        the Empty exception if no item was available within that time.
        Otherwise ('block' is false), return an item if one is immediately
        available, else raise the Empty exception ('timeout' is ignored
        in that case).
        """
        self.not_empty.acquire()
        try:
            if not block:
                if not self._qsize():
                    raise Empty
            elif timeout is None:
                while not self._qsize():
                    self.not_empty.wait()
            elif timeout < 0:
                raise ValueError("'timeout' must be a non-negative number")
            else:
                endtime = _time() + timeout
                while not self._qsize():
                    remaining = endtime - _time()
                    if remaining <= 0.0:
                        raise Empty
                    self.not_empty.wait(remaining)
            item = self._get()
            self.not_full.notify()
            return item
        finally:
            self.not_empty.release()

    # 非阻塞的get
    def get_nowait(self):
        """Remove and return an item from the queue without blocking.
        Only get an item if one is immediately available. Otherwise
        raise the Empty exception.
        """
        return self.get(False)

    # Override these methods to implement other queue organizations
    # (e.g. stack or priority queue).
    # These will only be called with appropriate locks held

    # Initialize the queue representation
    def _init(self, maxsize):
        # 在Queue中，底层数据结构是双端队列
        self.queue = deque()

    # 返回队列中的元素数
    def _qsize(self, len=len):
        return len(self.queue)

    # Put a new item in the queue
    def _put(self, item):
        # 在这里，把元素保存到底层的数据结构中
        self.queue.append(item)

    # Get an item from the queue
    def _get(self):
        return self.queue.popleft()



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
index(x[, start[, stop]])  找出x的index，或者从start 到stop之间找
insert(i, x)               在第i个位置插入x
pop()                      弹出队列最右边的元素
popleft()                  弹出队列最左边的元素
remove(value)              删除队列中从左数出现的第一个等于value的元素，如果找不到就报错
reverse()                  
rotate(n=1)
maxlen





