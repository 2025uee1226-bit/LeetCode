class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        p=[]
        k = k%(len(nums))
        p=nums [-k:] + nums[:-k]
        for i in range(len(nums)):
            nums[i]=p[i]
        
        return nums
        
        
        