class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return any"""
        p=[]
        hashmap=[0]*3
        for i in nums:
            hashmap[i]+=1
        for j in range(3):
            p.extend([j]*hashmap[j])
        for z in range(len(p)):
            nums[z]=p[z]
        return nums