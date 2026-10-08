class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        
        
        count=0
        if n>=1000:
            for i in range(1000,n+1):
                count+=(len(str(i))-1)//3
            return count
        return 0"""
        if n>999:
            return n-999
        return 0