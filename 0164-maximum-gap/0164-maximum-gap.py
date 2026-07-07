class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=0
        i=0
        p=0
        nums.sort()
        for j in range(1,len(nums)):
            i=j-1
            p=nums[j]-nums[i]
            m=max(m,p)
        return m