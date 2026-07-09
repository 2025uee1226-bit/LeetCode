class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n<=0 :
            return False
        else:
            i=0
            while 2**i<=n:
                if 2**i==n:
                    return True
                
                i+=1
        return False
        
        