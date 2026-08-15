class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        
        lst=[]
        count=Counter(nums)
        for num in nums:
            if count[num]>1:
                lst.append(num)
        return list(set(lst))"""
        s=set()
        s1=[]
        for num in nums:
            if num not in s:
                s.add(num)
            else:
                s1.append(num)
        return s1