class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        vowels="aeiou"
        count=Counter(s)
        vmax=0
        cmax=0
        
        for c ,freq in count.items():
            if c not in vowels:
                cmax=max(cmax,freq)
            else:
                vmax=max(vmax,freq)
        return vmax+cmax
                


        