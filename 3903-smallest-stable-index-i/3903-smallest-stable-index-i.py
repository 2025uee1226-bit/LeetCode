class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        diff=0
      
        for i in range(len(nums)):
            mx=max(nums[0:i+1])
            mn=min(nums[i:n])
            diff= mx-mn
            if diff <=k:
                return i
        return -1