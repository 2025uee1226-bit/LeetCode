class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        i=1
        if n ==1:
            return 0
        elif nums[n-1]>nums[n-2]:
            return n-1
        elif nums[1]<nums[0]:
            return 0
        else:
            for i in range(1,len(nums)-1):
                if nums[i-1]<nums[i]>nums[i+1]:
                    return i 
