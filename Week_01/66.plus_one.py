class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 没看答案前的思路
        # "".join(list) 这个list里面的元素只能是str才行
        # 不能直接list 整数，只能list str
        return list(str(int("".join([str(i) for i in digits]))+1))
        
    
        
        
        
        
        