class Solution(object):
    def reverse(self, n):
        """
        :type x: int
        :rtype: int
        """
        sign=-1 if n<0 else 1
        p=0
        m=abs(n)
        while(m!=0):
            
            p=p*10+m%10
            m=m//10
        if p<-2**31 or p>2**31-1:
            return 0
        else:
            return p*sign
    

    

            
        