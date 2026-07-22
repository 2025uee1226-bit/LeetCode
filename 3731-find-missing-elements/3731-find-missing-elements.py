class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums=list(set(nums))
        p=[x  for x in range(min(nums),max(nums)+1) if x not in nums]
        return p
        