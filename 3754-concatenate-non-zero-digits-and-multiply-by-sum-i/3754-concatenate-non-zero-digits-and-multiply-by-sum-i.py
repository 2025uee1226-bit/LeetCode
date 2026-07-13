class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        p=str(n)
        s=0
        r=""
        if n==0:
            return 0
        else:
            for  i in range(len(p)):
                if p[i]!="0":
                    r+=p[i]
                    s+=int(p[i])
        
            return int(r)*s


