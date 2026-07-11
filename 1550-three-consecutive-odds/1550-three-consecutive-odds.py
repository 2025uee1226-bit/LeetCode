class Solution(object):
    def threeConsecutiveOdds(self, nums):
        """
        :type arr: List[int]
        :rtype: bool
        """
        l=0
        
        while(l+2<len(nums)):
            if  nums[l]%2!=0 and nums[l+1]%2!=0 and nums[l+2]%2!=0:
                return True
            else:
                
                l+=1
        return False
        