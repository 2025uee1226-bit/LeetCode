class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        p=""
        for i in range(len(s)):
            if s[i]=="#":
                p*=2
            elif s[i]=="*":
                p=p[:-1]
            elif s[i]=="%":
                p=p[::-1]
            else:
                p+=s[i]
        return p
        