class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        c=0
        minm,maxm=len(nums),0
        for i in range(len(nums)):
            if nums[i]==target:
                c+=1
                minm=min(minm,i)
                maxm=max(maxm,i)
        if c==0:
            return [-1,-1]
        elif c==1:
            return [maxm,maxm]
        else:return [minm,maxm]
            
        