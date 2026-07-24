class Solution(object):
    def mostWordsFound(self, sentence):
        """
        :type sentences: List[str]
        :rtype: int
        """
        c=0
        m=0
        for i in range(len(sentence)):
            sentence[i]=sentence[i].strip()
            c=0
            for w in sentence[i]:
                if w==" ":
                    c+=1
            m=max(m,c+1)
        return m
