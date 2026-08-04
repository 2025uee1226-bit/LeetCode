class Solution(object):
    def lastStoneWeight(self, nums):
        """
        :type stones: List[int]
        :rtype: int
        """
       
        if len(nums)==1:
            return nums[0]
        else:
            while(len(nums))>1:
                nums.sort()
                y=nums.pop()
                x=nums.pop()
                if x!=y:
                    nums.append(y-x)
            return nums[0] if nums else 0