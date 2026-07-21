class Solution(object):
    def transformArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p=[]
        for i in nums:
            if i%2==0:
                p.append(0)
            else:
                p.append(1)
        return sorted(p)