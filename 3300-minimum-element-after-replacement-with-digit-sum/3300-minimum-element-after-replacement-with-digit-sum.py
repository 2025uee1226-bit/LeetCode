class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=0
        p=[]
        for i in range(len(nums)):
            s=0
            while(nums[i]>0):
                n=nums[i]%10
                s=s+n
                nums[i]//=10
            p.append(s)
        return min(p)
