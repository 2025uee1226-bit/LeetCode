class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        l=0
        m=1
        r=len(nums)
        while(l<r):
            if nums[l]==nums[m]:
                return nums[l]
            else:
                m+=1
                l+=1



        