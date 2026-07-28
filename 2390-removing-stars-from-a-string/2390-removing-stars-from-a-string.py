class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        hashset=[]
        for i in range(len(s)):
            if s[i]=="*":
                hashset.pop()
            else:
                hashset.append(s[i])
        return "".join(hashset)

        