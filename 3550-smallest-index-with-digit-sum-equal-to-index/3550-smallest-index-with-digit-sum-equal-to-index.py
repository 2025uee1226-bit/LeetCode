class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
    
        p=0
        
        for i in range(len(nums)):
            p=nums[i]
            s=0
            while(p>0):
                s+=p%10
                p=p//10
            if i==s:
                return i
        return -1"""
        for i in range(len(nums)):
            s=0
            for z in str(nums[i]):
                s+=int(z)
            if s==i:
                return i
        return -1

