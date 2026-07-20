class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        """
        :type nums: List[int]
        :type digit: int
        :rtype: int
        """
        c=0
        for num in nums:
            for d in str(num):
                if d == str(digit):
                    c+=1
        return c