class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0,len(nums)):
            c=nums[i]
            x=target-c
            if x in nums and nums.index(x)!=i:
                    list=[i,nums.index(x)]
                    return list


