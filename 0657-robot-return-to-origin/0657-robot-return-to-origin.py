class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        u=0
        d=0
        r,l=0,0
        for i in range(len(moves)):
            if moves[i]=="U":
                u+=1
            elif moves[i]=="D":
                d+=1
            elif moves[i]=="R":
                r+=1
            else:
                l+=1
        return u==d and r==l
        