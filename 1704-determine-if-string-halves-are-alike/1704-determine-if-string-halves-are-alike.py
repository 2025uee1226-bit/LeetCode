class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        
        c1,c2=0,0
        vow=['a','e','i','o','u','A','E','I','O','U']
        l=len(s)
        first=s[0:l//2]
        second=s[l//2:]
        for v in vow:
            for i in first:
                if v==i:
                    c1+=1
            for i in second :
                if v==i:
                    c2+=1
        return c1==c2"""
        l=len(s)
        first=s[0:l//2]
        second=s[l//2:]
        c1,c2=0,0
        for i in first:
            if i in "aeiouAEIOU":
                c1+=1
        for i in second:
            if i in "aeiouAEIOU":
                c2+=1
        return c1==c2



        