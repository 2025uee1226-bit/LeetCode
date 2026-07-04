class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        p=nums1+nums2
        p.sort()
        d=len(p)
        if d%2==1:
            return p[d//2]
        else: return (p[d//2-1]+p[d//2])/2.0
        
        