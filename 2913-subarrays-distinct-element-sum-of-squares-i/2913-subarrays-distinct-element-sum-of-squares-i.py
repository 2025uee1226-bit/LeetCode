class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum=0
        for i in range(0,len(nums)):
            for j in range(i,len(nums)):
                p=nums[i:j+1]
                s=set(p)
                sum+=(len(s)**2)
        return sum



        