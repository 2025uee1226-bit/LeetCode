class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        
        s=set()
        for num in sentence:
            s.add(num)
        return len(s)==26"""
        return len(set(sentence))==26
        
        