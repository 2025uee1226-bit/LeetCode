class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        u=[]
        nums.sort()
        for n in range(len(nums)):
            if nums[n]==target:
                u.append(n)
        return u
        