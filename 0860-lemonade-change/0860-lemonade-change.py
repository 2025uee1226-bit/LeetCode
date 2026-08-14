class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five,ten,twenty=0,0,0
        for num in bills:
            if num==5:
                five+=1
            elif num==10 and five>0:
                five-=1
                ten+=1
            elif num==20 and five>0 and ten>0:
                five-=1
                ten-=1
            elif num==20 and five>2:
                five-=3
            else:
                return False
        return True