class Solution(object):
    def mirrorDistance(self, n):
        """
        :type n: int
        :rtype: int
        """
        p=str(n)
        p=p[::-1]
        return abs(n-int(p))
        