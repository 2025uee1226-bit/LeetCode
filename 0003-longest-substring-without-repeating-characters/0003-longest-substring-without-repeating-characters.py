class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """

        :type s: str
        :rtype: int
        """
        l=0
        
        for i in range(len(s)):
            p=""
            for j in range(i,len(s)):
                if s[j] not in p:
                    p+=s[j]
                else:
                    l=max(l,len(p))
                    
                    break
            l=max(l,len(p))
                    
        return l
                    


                

        