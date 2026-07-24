class Solution(object):
    def digitFrequencyScore(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        hashset=[0]*10
        for num in str(n):
            hashset[int(num)]+=1
        s=0
        for digit,frequency  in enumerate(hashset):
            s+=digit*frequency
        return s

        