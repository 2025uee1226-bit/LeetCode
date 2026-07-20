class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        less,great,equal=[],[],[]
        
        for i in range (len(nums)):
            if nums[i] < pivot:
                less.append(nums[i])
            elif nums[i] > pivot:
                great.append(nums[i])
            else:
                equal.append(nums[i])
        
        return less+equal+great