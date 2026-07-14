class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        leftsum=[]
        rightsum=[]
        
        for i in range(len(nums)):
            s=0
            for j in range(i+1,len(nums)):
                s=s+nums[j]
            rightsum.append(s)
        for z in range(len(nums)-1,-1,-1):
            s=0
            for m in range(z-1,-1,-1):
                s+=nums[m]
            leftsum.append(s)
        leftsum.reverse()
        p=[abs(leftsum[i]-rightsum[i]) for i in range(len(nums))]
        return p
                
        