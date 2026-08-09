class Solution(object):
    def smallestAbsent(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=1
        sm=sum(nums)
        n=len(nums)
        avg=sm//n
        while(True):
            if i> avg and i not in nums:
                return i
            else:
                i+=1

        