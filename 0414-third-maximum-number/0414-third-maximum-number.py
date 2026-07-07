class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=list(set(nums))
        a.sort()
        if len(a)>2:
            return a[-3]
        else:
            return a[-1]