class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        p = list(set(nums))
        return len(p) != len(nums)


        