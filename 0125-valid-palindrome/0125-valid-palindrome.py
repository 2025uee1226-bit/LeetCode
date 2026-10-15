class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        news=""
        result=s.replace(" ","")
        for i in result:
            if i.isalnum():
                news+=i
        return news==news[::-1]
        