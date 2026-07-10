class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=0
        b=1
        sum=0
        if n>1:
            for i in range(n-1):
                sum=a+b
                a=b
                b=sum
            return sum
        elif n==1:
                return 1
        else:return 0