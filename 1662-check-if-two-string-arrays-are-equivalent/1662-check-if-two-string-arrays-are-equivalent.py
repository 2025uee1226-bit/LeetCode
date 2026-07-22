class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        s=""
        p=""
        for i in range(len(word1)):
            s+=word1[i]
        for j in range(len(word2)):
            p+=word2[j]
        return s==p
