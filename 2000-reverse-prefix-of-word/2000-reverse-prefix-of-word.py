class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        if ch in word:
            first=word.index(ch)
            word=word[first::-1]+word[first+1:]
            return word
        else:
            return word