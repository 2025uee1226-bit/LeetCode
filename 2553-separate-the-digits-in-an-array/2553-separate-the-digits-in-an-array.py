class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List
        """
        c=[]
        for x in nums:
            for d in str(x):
                c.append(int(d))

        return c