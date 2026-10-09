class Solution(object):
    def reverse(self, n):
        """
        :type x: int
        :rtype: int
        
        sign=-1 if n<0 else 1
        p=0
        m=abs(n)
        while(m!=0):
            
            p=p*10+m%10
            m=m//10
        if p<-2**31 or p>2**31-1:
            return 0
        else:
            return p*sign"""
        sign=0
        s=""
        rev=""
        if n<0:
            sign=-1
        else:
            sign=1
        m=abs(n)
        s=str(m)
        rev=s[::-1]
        if int(rev)<-2**31 or int(rev)>2**31-1:
            return 0
        else:
            return int(rev)*sign
        
    

    

            
        