class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        
        c=0
        for i in range(len(nums)):
            if target==nums[i]:
                c=+1
        return c>=1"""
        return target in nums
        