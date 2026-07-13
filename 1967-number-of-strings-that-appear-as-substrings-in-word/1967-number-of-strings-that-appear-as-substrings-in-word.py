class Solution(object):
    def numOfStrings(self, pattern, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        c=0
        for i in range(len(pattern)):
            if pattern[i] in word:
                c+=1
        return c