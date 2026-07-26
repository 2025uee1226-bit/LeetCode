class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int"""
        
        m=0
        
        p=min(nums)
        s=max(nums)
        for i in range(1,s+1):
            if p%i==0 and s%i==0:
                m=max(i,m)
        return m
        """mx=0
        for i in range(1,max(nums)+1):
            if max(nums)%i==0 and min(nums)%i==0:
                mx=max(mx,i)
        return mx"""
        ###if min(nums)%2==0 and max(nums)%2!=0:
           # return max(nums)%min(nums)
        #elif min(nums)%2!=0 and max(nums)%2==0:
          #  return 1
        #elif max(nums)%min(nums)==0:
           # return min(nums)
