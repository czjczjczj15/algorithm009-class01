

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        #####################Attention, do not modify nums,so the solution below is wrong####
        # count = 0
        # temp = nums
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         temp.pop(count)
        #         temp.append(0)
        #     else:
        #         count +=1
        #     print(i, nums[i], temp, nums, count)
        # return temp
        
        ###############
        # 第一次：
        # my code
        # count = 0
        # for i in range(len(nums)):
        #     if nums[count] == 0:
        #         temp = nums[count]
        #         nums.pop(count)
        #         nums.append(0)
        #     else:
        #         count += 1
        
        ###第二次：
        # 法一：两个for loop，删除0的同时记录0的个数，然后第二个for loop加上
        # 发二：创建新的数组，但是这题不允许
        # 法三：加一个j来记录0的位置，然后与非0的值换位置
        
        # 法三的方法
        # j = 0
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         nums[j] = nums[i]
        #         if (j != i):
        #             nums[i] = 0
        #         j += 1
        # i走得比j快，j在最后一个非零的位置上，然后的值都应该赋值为0
                
        # 其实想第一种方法那样用pop也是ok的，只要pop完立刻加回来的话，
        # for loop的len就不会变
        
        # 比第一次的代码看上去更加简单，但是当删除一个元素的时候，时间复杂度很高：
        # for i in nums:
        #     if i ==0:
        #         nums.remove(i)  # 时间复杂度是O(n) (其实应该每次的数量递减，但是看做n)
        #         nums.append(0)  # 时间复杂度是O(1)
        # 所以还是交换的方法好一点，空间和时间都低 
        
        # 下面这样不行，这样会元素跳着走，虽然pop比remove快
        # pop 比 del快，del 比remove 快， https://zhuanlan.zhihu.com/p/75321136
        # for i in range(len(nums)):
        #     if nums[i] ==0:
        #         nums.pop(i)
        #         nums.append(0)
        
        # 国际站的python solution
        zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
        # python的两个量交换是不需要中间值的
            
        
        
        
            
        
        
                
                
                
                
        