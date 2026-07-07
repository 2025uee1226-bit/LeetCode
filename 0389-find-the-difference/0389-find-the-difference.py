class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        j=0
        i=0
        s=sorted(s)
        t=sorted(t)
        while(i<len(s)):
            if s[i]!=t[j]:
                return t[j]
            i+=1
            j+=1
        j+=1
        if j>i:
            return t[-1]