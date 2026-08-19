class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        n1=nums[:n]
        n2=nums[n:]
        nums_new=[]
        for i in range(len(n1)):
            nums_new.append(n1[i])
            nums_new.append(n2[i])
        return nums_new