class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        #将arr1 counter计数，按照arr2来取
        li = []
        counter = collections.Counter
        count = counter(arr1)
        #按照arr2将arr1的元素存入li
        for val in arr2:
            if val in count:
                l = count[val]
                print(l)
                for i in range(l):
                    li.append(val)
            #被存的元素删除掉
            del count[val]
        #剩下的元素排序放到末尾
        li += sorted(list(count.elements()))
        return li