class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=0
        i,j=0,1
        nums.sort()
        while j<len(nums):
            m=max(m,nums[j]-nums[i])
            i+=1
            j+=1
        return m