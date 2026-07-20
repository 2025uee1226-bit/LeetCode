class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        less,great,equal=[],[],[]
        
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num > pivot:
                great.append(num)
            else:
                equal.append(num)
        
        return less+equal+great