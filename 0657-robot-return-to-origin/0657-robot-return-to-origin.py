class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        u,r,l,d=0,0,0,0
    
        for i in range(len(moves)):
            if moves[i]=="U":
                u+=1
            elif moves[i]=="D":
                d+=1
            elif moves[i]=="R":
                r+=1
            else:
                l+=1
        f= (u==d and r==l)
        return f
        