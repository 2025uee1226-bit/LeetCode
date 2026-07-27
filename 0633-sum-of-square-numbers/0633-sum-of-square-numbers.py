class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        r=int(c**(0.5))
        l=0
        while(l<=r):
            p=l**2
            z=r**2
            if z+p==c:
                return True
            elif z+p>c:
                r-=1
            elif z+p<c:
                l+=1
        return False

        