class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum=0
        for i in range(len(s)):
            p=122-ord(s[i])+1
            sum+=(p*(i+1))
        return sum