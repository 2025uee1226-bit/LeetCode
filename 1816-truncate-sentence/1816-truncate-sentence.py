class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        p=s.split()
        m=p[:k]
        return " ".join(m)
        