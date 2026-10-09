class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        u=[]
        for i in range(len(nums)):
            if val!=nums[i]:
                    u.append(nums[i])
        for j in range(len(u)):
            nums[j]=u[j]
        return len(u)