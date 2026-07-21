class Solution(object):
    def transformArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p=[0  if x%2==0  else 1 for x in nums] 
        return sorted(p)