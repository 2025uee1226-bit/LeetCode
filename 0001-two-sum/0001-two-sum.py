class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        p=0
        c=[]
        for i in range(len(nums)):
            p=target-nums[i]
            for j in range(i+1,len(nums)):
                if p == nums[j]:
                    c.append(i)
                    c.append(j)
                
        return c
            




