class Solution(object):
    def sumAndMultiply(self, p):
        """
        :type n: int
        :rtype: int
        """
        p=str(p)
        s=0
        r=""
        if p=="0":
            return 0
        else:
            for  i in range(len(p)):
                if p[i]!="0":
                    r+=p[i]
                    s+=int(p[i])
        
            return int(r)*s


