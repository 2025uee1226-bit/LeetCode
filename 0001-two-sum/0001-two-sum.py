class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            req=target-nums[i]
            if req in nums and i!=nums.index(req):
                return [i,nums.index(req)]
        


