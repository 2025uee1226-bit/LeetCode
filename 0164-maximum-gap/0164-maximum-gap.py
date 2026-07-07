class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=0
        i,j,p=0,1,0
        nums.sort()
        while j<len(nums):
            p=nums[j]-nums[i]
            m=max(m,p)
            i+=1
            j+=1
        return m