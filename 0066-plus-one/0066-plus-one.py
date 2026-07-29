class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        
        p=0
        u=[]
        d=len(digits)
        for i in range(len(digits)):
            p=p+digits[i]*(10**(d-1))
            d-=1
        p=p+1
        while p>0:
            u.append(p%10)
            p=p//10
        return u[::-1]"""
       
        for i in range(len(digits)-1,-1,-1):
            if digits[i]!=9:
                digits[i]+=1
                return digits
            digits[i]=0
        return [1]+digits
            



