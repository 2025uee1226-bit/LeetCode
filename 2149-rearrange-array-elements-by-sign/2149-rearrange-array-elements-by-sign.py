class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p=[]
        z=[]
        s=[]
        for num in nums:
            if num<0:
                p.append(num)
            else:
                z.append(num)
        for j in range(len(nums)):
            if j%2==0:
                s.append(z[j//2])
            else:
                s.append(p[(j-1)//2])
        return s