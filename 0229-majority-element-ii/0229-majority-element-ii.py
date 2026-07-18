class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s=len(nums)
        hashset=Counter(nums)
        return [x for x in hashset if hashset[x]> s//3]
        
        