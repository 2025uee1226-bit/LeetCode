class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        p=[]
        for i in range(len(arr)):
            
            if arr[i]==0:
                p.append(0)
                p.append(0)
            else:
                p.append(arr[i])
        for z in range(len(arr)):
            arr[z]=p[z]
        return arr


        