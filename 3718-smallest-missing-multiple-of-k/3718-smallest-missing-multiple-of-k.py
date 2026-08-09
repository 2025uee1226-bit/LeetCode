class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i=1
        while(True):
            if k*i in nums:
                i+=1
            else:
                return k*i
        