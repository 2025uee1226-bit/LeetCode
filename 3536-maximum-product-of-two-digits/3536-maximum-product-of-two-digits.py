class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        p,z=0,[]
        while(n>0):
            p=n%10
            z.append(p)
            n=n//10
        z.sort()
        return z[-1]*z[-2]

        