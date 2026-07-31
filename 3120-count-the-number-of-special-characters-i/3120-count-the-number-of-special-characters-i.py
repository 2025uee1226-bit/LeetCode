class Solution(object):
    def numberOfSpecialChars(self, nums):
        """
        :type word: str
        :rtype: int
        """
        p=""
        z=""
        s=set()
        
        for i in range(0,len(nums)):
            p=nums[i].upper()
            z=nums[i].lower()
            if p in nums and z in nums:
                s.add(z)
            
                
        return len(s)
            
        