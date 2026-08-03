class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        p=s.strip()
        z=p.split()
       
        l=0
        r=len(z)-1
        while(l<=r):
            z[l],z[r]=z[r],z[l]
            l+=1
            r-=1
        return " ".join(z)        

        