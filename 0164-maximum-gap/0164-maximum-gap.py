class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        

        p=0
        m=0
        nums.sort()
        for j in range(1,len(nums)):
            p=nums[j]-nums[j-1]
            m=max(m,p)
        return m