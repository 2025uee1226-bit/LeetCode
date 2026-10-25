class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        
        rem=sum(nums)%k
        return rem"""
        return sum(nums)%k

        