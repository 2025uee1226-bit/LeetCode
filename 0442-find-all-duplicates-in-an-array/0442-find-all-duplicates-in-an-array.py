class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        z=[]
        hash_map=[0]*(len(nums)+1)
        for c in nums:
            hash_map[c]+=1
        for i in range(len(hash_map)):
            if hash_map[i]==2:
                z.append(i)
        return z


        