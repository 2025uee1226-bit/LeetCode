class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        sum=0
        n=len(nums)
        for i in range (0,n) :
            sum=sum+nums[i]
        return n*(n+1)//2-sum"""
        hashset=[0]*(len(nums)+1)
        for num in nums:
            hashset[num]+=1
        return hashset.index(0)
        