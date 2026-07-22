class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int"""
    
        u=[]
        for x in nums:
            if x not in u :
                u.append(x)
        for i in range (len(u)):
            nums[i]=u[i]
        return len(u)