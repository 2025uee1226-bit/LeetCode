class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        div,ndiv=[],[]
        for i in range(1,n+1):
            if i%m==0:
                div.append(i)
            else:
                ndiv.append(i)
        return sum(ndiv)-sum(div)