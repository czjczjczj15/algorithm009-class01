# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        #法一：迭代法
        #法二：回归recursion 
        #法三: in-place? 
        
        # 第一次不会，看的答案：
        # prev = dummy = ListNode(None)
        # while l1 and l2:
        #     if l1.val < l2.val:
        #         prev.next = l1 #为什么这里不会把一串都给赋值进来？
        #         l1 = l1.next
        #     else:
        #         prev.next = l2
        #         l2 = l2.next
        #     prev = prev.next
        # prev.next = l1 or l2 # 这里用or的话就可以哪个不是None就连哪个
        # print(l1 or l2)
        # a = [1,2,3]
        # b = [2,3]
        # print(a or b)
        # return dummy.next
    
        # 第二次：还不会创建一个 linked list
        # 记住是 = ListNode(None)
        # 先是用XXX.next 指向另一个linked list，直接指就好了
        #，因为直接指是代表指向那个list的现在当前的node。
        # 然后再XXX = XXX.next 更新XXX这个list的现在的node, 这题相当于增加这个空的list
        # 因为如果当前的Node往后移动了，就有点难回到第一个，所以直接用dummy作为令一个当前的node
        # 这里prev.next = l1 or l2表明 l1, l2既是当前的node，也是一串node?  
       
        # recursively 1
        # If both lists are non-empty, I first make sure a starts smaller, use its head as result, and merge the remainders behind it. Otherwise, i.e., if one or both are empty, I just return what's there.
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        print(l1 or l2)
        return l1 or l2
    
        # First make sure that a is the "better" one (meaning b is None or has larger/equal  value). Then merge the remainders behind a.
        # if not l1 or l2 and l1.val > l2.val:
        #     l1, l2 = l2, l1
        # if l1:
        #     l1.next = self.mergeTwoLists(l1.next, l2)
        # return l1
        
        
        #备注： 在 Python 中，and 和 or 都有提前截至运算的功能。
        # and：如果 and 前面的表达式已经为 False，那么 and 之后的表达式将被 跳过，返回左表达式结果
        # or：如果 or 前面的表达式已经为 True，那么 or 之后的表达式将被跳过，直接返回左表达式的结果
        # 例子：[] and 7 等于 []
        # a = [1,2,3]
        # # a = []
        # b = [4,5,6]
        # # b = []
        # print(a or b)
