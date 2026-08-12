class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int"""
        
        mn=len(nums)
        for i in range(len(nums)):
            if nums[i]==target:
                mn=min(mn,abs(i-start))
        return mn


        