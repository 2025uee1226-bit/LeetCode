class Solution(object):
    def reverse(self, n):
        """
        :type x: int
        :rtype: int
        """
        p,z=0,0
        m=abs(n)
        while(m!=0):
            z=m%10
            p=p*10+z
            m=m//10
        if p<-2**31 or p>2**31-1:
            return 0
        elif n<0:
            return -p
        else:return p

    

            
        