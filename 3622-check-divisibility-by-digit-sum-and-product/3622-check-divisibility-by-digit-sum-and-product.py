class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sum=0
        product=1
        for s in str(n):
            product=product*int(s)
            sum+=int(s)
        if n%(sum+product)==0:
            return True
        else:
            return False
        