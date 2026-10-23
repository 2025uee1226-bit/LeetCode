class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        v="AEIOUaeiou"
        i=2
        p=[]
        words=sentence.split()
        for s in words:
            if s[0] in v:
                s+="m"+"a"*i
                i+=1
            else:
                s=s[1:]+s[0]
                s+="m"+"a"*i
                i+=1
            p.append(s)
        return " ".join(p)