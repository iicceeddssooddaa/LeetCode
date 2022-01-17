##第一种
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j] == target):
                    return ([i,j])
        #速度太慢

-----------------------
##第二种
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums) - 1):
            newtarget = target - nums[i]
            for j in range(i + 1, len(nums)):
                if (nums[j] == newtarget):
                    return ([i,j])
        #略有进步。嵌套循环依然复杂

-----------------------
## 第三种
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
Dict = {}
        for index, i in enumerate(nums):
            if i in Dict:
                return ([Dict.get(i),index])
            newtarget = target - i
            Dict[newtarget] = index
        #Thanks to TF.
        #核心在于Dictionary使用。通过回顾搜索是否存在匹配，并在同一循环中增补新的条目。利用索引可查这一特点。

---------------------
---------------------
#构建字典
Dict = {}
        for index, i in enumerate(nums):
            if i in Dict:
                return ([Dict.get(i),index])
            newtarget = target - i
            Dict[newtarget] = index
