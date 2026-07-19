class Solution(object):
    def heightChecker(self, height):
        """
        :type heights: List[int]
        :rtype: int
        """
        expected=sorted(height)
        c=0
        for i in range(len(height)):
            if expected[i]!=height[i]:
                c+=1
        return c
        