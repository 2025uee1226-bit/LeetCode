class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<1:
            return False
        else:
            while n%4==0:
                n=n//4
            return n==1
        