class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: 
        
        l=0
        j=0
        r=0
        s=""
        while(r<len(needle)):
            if haystack[l]==needle[r]:
                s+=haystack[l]
                l+=1
                r+=1
            else:
                l+=1
        if s==needle:
            return needle.index(haystack[0])
        else:return -1"""
        p=""
        if needle in haystack:
            return haystack.find(needle)
        return -1


            
            