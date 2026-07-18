class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=0
        nums.sort()
        p=nums[0]
        s=nums[-1]
        for i in range(1,s+1):
            if p%i==0 and s%i==0:
                m=max(i,m)
        return m
        