class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        n=str(num)
        l=0
        new_num=""
        while(l<len(n)):
            if n[l]=="9":
                new_num+="9"
            else:
                new_num+="9"
                break
            l+=1
        new_num+=n[l+1:]
        return int(new_num)
        
      