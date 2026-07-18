class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p=""
        s=0
        for i in range(len(nums)):
            p=str(nums[i])
            if len(p)%2==0:
                s+=1 
        return s
        