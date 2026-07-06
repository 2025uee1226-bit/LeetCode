class Solution(object):
    def addDigits(self, n):
        """
        :type num: int
        :rtype: int
        """
        
        while n>9:
            s=0
            while n>0:
                s=s+n%10
                n=n//10
            n=s
        return n
        