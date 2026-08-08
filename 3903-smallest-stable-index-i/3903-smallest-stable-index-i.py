class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
      
        for i in range(len(nums)):
            mx=max(nums[0:i+1])
            mn=min(nums[i:n])
            if mx-mn<=k:
                return i
        return -1