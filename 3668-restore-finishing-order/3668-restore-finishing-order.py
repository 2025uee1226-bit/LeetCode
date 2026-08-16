class Solution(object):
    def recoverOrder(self, order, friends):
        """
        :type order: List[int]
        :type friends: List[int]
        :rtype: List[int]
        
        arr=[]
        for num in order:
            if num in friends:
                arr.append(num)
        return arr"""
        arr=[num  for num in order if num in friends]
        return arr

        