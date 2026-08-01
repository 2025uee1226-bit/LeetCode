class Solution(object):
    def countSymmetricIntegers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        count=0
        
        for i in range(low,high+1):
           s=str(i)
           n=len(s)
           
           if n%2==0:
            half=n//2
            first=sum(int(digits) for digits in s[:half])
            second=sum(int(digits)for digits in s[half:])
            if first==second:
                count+=1
        return count