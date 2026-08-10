class Solution(object):
    def largestEven(self, s):
        """
        :type s: str
        :rtype: str
        """
        l=0
        r=len(s)-1
        while(l<=r):
            if int(s[l:r+1])%2==0:
                return s[l:r+1]
            elif s[r]=="1":
                r-=1
            else:
                l+=1
        return ""
        