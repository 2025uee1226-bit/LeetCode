class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p=max(nums)
        nums.remove(p)
        n=max(nums)
        return (p-1)*(n-1)

        