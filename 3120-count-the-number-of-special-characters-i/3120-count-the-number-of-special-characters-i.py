class Solution(object):
    def numberOfSpecialChars(self, nums):
        """
        :type word: str
        :rtype: int
        """
        p=""
        z=""
        s=set()
        for j in range(len(nums)):
            for i in range(j+1,len(nums)):
                p=nums[i].upper()
                z=nums[i].lower()
                if p in nums and z in nums:
                    s.add(z)
                    
        return len(s)
            
        