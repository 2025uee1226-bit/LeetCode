class Solution(object):
    def addToArrayForm(self, nums, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        p=""
        s,m=0,0
        arr=[]
        for  i in range(len(nums)):
            p+=str(nums[i])
        p=int(p)
        s=p+k
        while s>0:
            m=s%10
            arr.append(m)
            s//=10
        return arr[::-1]