class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        final=nums[-1]*nums[-2]*nums[-3]
        initial=nums[0]*nums[1]*nums[-1]
        return max(final,initial)

        
        