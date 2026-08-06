class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """

        for i in range(n,n+11):
            num=i
            product=1
            while num>0:
                product*=num%10
                num//=10
            if product%t==0:
                return i
        

        