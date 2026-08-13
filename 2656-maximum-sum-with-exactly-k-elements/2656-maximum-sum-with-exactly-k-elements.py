class Solution(object):
    def maximizeSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mx=max(nums)
        sum=0
        for i in range(k):
            sum+=mx
            mx+=1
        return sum
        