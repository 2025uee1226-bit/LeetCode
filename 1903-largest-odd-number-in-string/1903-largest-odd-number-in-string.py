class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        l=0
        r=len(num)
        
        while(l<=r):
            if int(num[r-1])%2 !=0:
                return num[l:r]
            else:
                r-=1
        return ""