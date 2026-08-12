class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s)==len(goal) and s==goal:
            return True
        elif goal in s:
            return False
        else:
            new_s=s+s+s
            return goal in new_s
            
        