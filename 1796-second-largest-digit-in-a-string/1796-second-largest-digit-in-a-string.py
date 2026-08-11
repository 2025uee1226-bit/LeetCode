class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        dig=set()
        for ch in s :
            if ch.isdigit():
                dig.add(int(ch))
        dig=list(dig)
        dig.sort(reverse=True)
        if len(dig)==1 or len(dig)==0:
            return -1
        else:
            return dig[1]