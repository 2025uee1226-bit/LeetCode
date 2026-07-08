class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        p=0
        z=0
        while n!=1 and n!=4:
            z=0
            while n>0:
                p=n%10
                z=z+p**2
                n=n//10
            n=z
            
        return n==1

        