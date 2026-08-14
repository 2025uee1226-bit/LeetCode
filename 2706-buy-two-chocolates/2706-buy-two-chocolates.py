class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        prices.sort()
        total=prices[0]+prices[1]
        if money >=total:
            return money-total
        else:
            return money