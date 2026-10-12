class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        real_sum=n*(n+1)//2
        array_sum=sum(nums)
        sumset=sum(list(set(nums)))
        duplicate=array_sum-sumset
        missing=real_sum-sumset
        return [duplicate,missing]

        