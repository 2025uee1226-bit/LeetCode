class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words=s.split()
        s1=""
        for num in words:
            s1+=num[::-1]+" "
        s2=s1.strip()
        return s2
        