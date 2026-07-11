class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p=[x**2 for x in nums]
        return sorted(p)
        