class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        s=""
        for ch in address:
            if ch==".":
                s+="[.]"
            else:
                s+=ch
        return s
        
        