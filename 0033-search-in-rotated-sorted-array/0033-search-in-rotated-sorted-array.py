class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        
        for i in range(len(nums)):
            if nums[i]==target:
                    return i
        return -1"""
        for num in nums:
            if num==target:
                return nums.index(target)
        return -1
        